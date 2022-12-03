import os
from requests import sessions
from pprint import pprint
from time import sleep
from rocketchat_API.rocketchat import RocketChat

username = os.environ.get('ROCKET_USERNAME')
password = os.environ.get('ROCKET_PASSWORD')
server_url = os.environ.get('ROCKET_SERVER_URL')

with sessions.Session() as session:
    rocket = RocketChat('Werewolf', 'Me1onpan#', server_url='http://rocketchat:3000', session=session)
    # pprint(rocket.me().json())
    # pprint(rocket.channels_list().json())
    # pprint(rocket.chat_post_message('aiueo', channel='GENERAL').json())
    # pprint(rocket.channels_history('GENERAL', count=5).json())

def run():
    while 1:
        message=rocket.channels_history('GENERAL',count=1).json() # dict型w
        message_format=message['messages'] # list型
        message_split=(message_format[0]['msg'])

        if message_split == 'あいうえお':
            pprint(rocket.chat_post_message('aiueo', channel='GENERAL').json())

        sleep(1)

if __name__ == '__main__':
    print('Bot started')
    run()