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

def get_message():# 最新のメッセージを取得
    message=rocket.channels_history('GENERAL',count=1).json() # dict型w
    message_format=message['messages'] # list型
    message_split=(message_format[0]['msg'])
    return message_split

def compare_message(message):# 一致する文章に返信
    if message == '私は人狼です':
        rocket.chat_post_message('お前殺す', channel='GENERAL')

    if message == '私は村人です':
        rocket.chat_post_message('黙れ', channel='GENERAL')

def run():
    rocket.chat_post_message('人狼ゲームを始めます', channel='GENERAL')

    # pprint(rocket.im_list().json()) # DM一覧を表示

    # rocket.chat_post_message('かす', room_id='LMce5yj9EHHMc4XeXfyNf7LGr3Z9fzxaXY') # chat_post_messageでroom_idを指定するとDM,channelを指定するとチャンネル

    while 1:
        message = get_message()
        compare_message(message)
        sleep(1)

if __name__ == '__main__':
    print('Bot started')
    run()