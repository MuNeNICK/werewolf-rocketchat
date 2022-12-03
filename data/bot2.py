import os
from RocketChatBot import RocketChatBot

# botname = os.environ['BOTNAME']
# botpassword = os.environ['BOTPASSWORD']
# server_url = os.environ['BOT_URL']

bot = RocketChatBot('Werewolf', 'Me1onpan#', 'http://rocketchat:3000')

bot.send_message('starting bot...', channel_id='general')
bot.add_auto_answer(['good news', 'i have good news', ], ['hell yeah!', 'tell me, tell me!', 'you are already good news ;)', ])
bot.add_direct_answer(['who are you?', 'what is your name?', ], ['I am botname', ])

if __name__ == '__main__':
    print('Bot started')
    bot.run()