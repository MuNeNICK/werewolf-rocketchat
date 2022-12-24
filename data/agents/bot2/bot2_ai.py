import openai
from .bot2 import bot2_rocket

openai.api_key = "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"

with open('agents/bot1/start.txt') as f:
    s = f.read()

def handle_response(message) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=
        s +
        ''' 
        GM: 
        '''
        + message +
        '''
        GM: ただし、役職が人狼の方は自身の役職が村人であると主張してください。
        BOT1: 
        '''
        ,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    responseMessage = response.choices[0].text

    return responseMessage

def bot2_intro():
    response = handle_response("自己紹介とあなたの役職を教えてください")
    bot2_rocket.chat_post_message(response, channel='GENERAL')