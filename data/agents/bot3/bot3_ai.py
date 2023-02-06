import os
import openai
import random
from .bot3 import bot3_rocket
from time import sleep,time

openai.api_key = os.environ.get('OPENAI_KEY')

with open('agents/bot3/start.txt') as f:
    start = f.read()

def handle_response(message) -> str:
    response = openai.Completion.create(
        # model="text-chat-davinci-002-20221122",
        model="text-davinci-003",
        prompt=
        message +
        '''
        あなた: 
        '''
        ,
        temperature=0.4,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0.0,
    )

    responseMessage = response.choices[0].text

    return responseMessage

def bot3_intro():
    response = handle_response(start + "GM: 自己紹介とあなたの役職を教えてください。ただし、役職が人狼の方は自身の役職が村人であると主張してください。")
    # response = handle_response(start + "GM: 自己紹介とあなたの役職を教えてください。ただし、役職が人狼の方は自身の役職が村人であると主張してください。")
    bot3_rocket.chat_post_message(response, channel='GENERAL')

def bot3_response(message):
    response = handle_response(start + "GM: 朝になりました。議論をはじめてください。他の人:" + message)
    bot3_rocket.chat_post_message(response, channel='GENERAL')
    sleep(1)

def bot3_vote():
    bot_list = ["BOT1", "BOT2", "BOT4", "BOT5", "BOT6"]
    random_num = random.randint(0, 4)
    bot_name = bot_list[random_num]
    bot3_rocket.chat_post_message('!vote @' + bot_name, channel='GENERAL')
    sleep(1)
