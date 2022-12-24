import openai
from .bot1 import bot1_rocket

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

def bot1_intro():
    response = handle_response("自己紹介とあなたの役職を教えてください")
    bot1_rocket.chat_post_message(response, channel='GENERAL')