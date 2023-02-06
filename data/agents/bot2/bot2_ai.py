import os
import openai
from .bot2 import bot2_rocket
from time import sleep,time

openai.api_key = os.environ.get('OPENAI_KEY')

with open('agents/bot2/start.txt') as f:
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
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0.0,
    )

    responseMessage = response.choices[0].text

    return responseMessage

def bot2_intro():
    response = handle_response(start + "GM: 自己紹介とあなたの役職を教えてください。ただし、役職が人狼の方は自身の役職が村人であると主張してください。")
    bot2_rocket.chat_post_message(response, channel='GENERAL')

def bot2_response(message):
    response = handle_response(start + "GM: 朝になりました。議論をはじめてください。他の人:" + message)
    bot2_rocket.chat_post_message(response, channel='GENERAL')
    sleep(1)