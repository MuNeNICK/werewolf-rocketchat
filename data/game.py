import sys
from pprint import pprint
from main import rocket

def start_game(message):
    if message == '!start':
        rocket.chat_post_message('人狼ゲームを始めます', channel='GENERAL')
        send_position()
        return 1

def stop_game(message):
    if message == '!stop':
        rocket.chat_post_message('人狼ゲームを終了します', channel='GENERAL')
        return 1

def get_message(): # 最新のメッセージを取得
    message = rocket.channels_history('GENERAL',count=1).json() # dict型 GENERALの最新メッセージを取得
    message_format = message['messages'] # list型
    message_split = message_format[0]['msg'] # str型 最新のメッセージを格納
    return message_split

def compare_message(message): # 一致する文章に返信
    if message == '私は人狼です':
        rocket.chat_post_message('お前が人狼だったのか', channel='GENERAL')

    if message == '私は村人です':
        rocket.chat_post_message('ふーん', channel='GENERAL')

def send_position():
    members = rocket.channels_members('GENERAL').json() # GENERALに参加しているメンバー一覧
    members_format = members['members']
    members_list  = []
    for member in members_format:
        members_list.append(member['username']) 
        if member['username'] != 'Werewolf':
            rocket.im_create(member['username']) # GENERALに参加しているメンバー全員のDMを作成
    
    dms = rocket.im_list().json() # DM一覧を表示
    dms_format = dms['ims']

    dms_users = []
    dms_id = []
    for dm_list in dms_format: # DM一覧からユーザ名とルームIDを抽出
        dms_users.append(dm_list['usernames'])
        dms_id.append(dm_list['_id'])

    dms_users_list = []
    for dm_users in dms_users: # ユーザ名からWerewolfを削除
        dms_users_list.append(dm_users[0])

    dms_dict = dict(zip(dms_users_list, dms_id)) # ユーザ名とルームIDを紐づけ(dict型)

    for member in members_list: # GENERALに参加しているメンバーのルームIDを検索
        if member != 'Werewolf':
            print(dms_dict[member])
            rocket.chat_post_message('かす', room_id=dms_dict[member]) # メンバー全員にメッセージを送信

def random_position():

