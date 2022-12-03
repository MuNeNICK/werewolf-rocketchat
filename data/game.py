from pprint import pprint
from main import rocket

def start_game():
    rocket.chat_post_message('人狼ゲームを始めます', channel='GENERAL')

def get_message():# 最新のメッセージを取得
    message=rocket.channels_history('GENERAL',count=1).json() # dict型 GENERALの最新メッセージを取得
    message_format=message['messages'] # list型
    message_split=(message_format[0]['msg']) # str型 最新のメッセージを格納
    return message_split

def compare_message(message):# 一致する文章に返信
    if message == '私は人狼です':
        rocket.chat_post_message('お前殺す', channel='GENERAL')

    if message == '私は村人です':
        rocket.chat_post_message('黙れ', channel='GENERAL')

# def send_position():
# pprint(rocket.im_list().json()) # DM一覧を表示
# rocket.chat_post_message('かす', room_id='LMce5yj9EHHMc4XeXfyNf7LGr3Z9fzxaXY') # chat_post_messageでroom_idを指定するとDM,channelを指定するとチャンネル