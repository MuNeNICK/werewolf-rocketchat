import random
from time import sleep,time
from pprint import pprint
from main import rocket

def start_game(message):
    if message == '!start':
        rocket.chat_post_message('人狼ゲームを始めます', channel='GENERAL')
        random_position()
        return 1

def stop_game(message):
    if message == '!stop':
        rocket.chat_post_message('人狼ゲームを終了します', channel='GENERAL')
        remove_werewolfs()
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

def find_members():
    members = rocket.channels_members('GENERAL').json() # GENERALに参加しているメンバー一覧
    members_format = members['members']
    members_list  = []
    for member in members_format:
        members_list.append(member['username']) 
        if member['username'] != 'Werewolf':
            rocket.im_create(member['username']) # GENERALに参加しているメンバー全員のDMを作成
    members_list.remove('Werewolf')
    return members_list

def find_user_id(channel):
    users = rocket.channels_members(channel).json() # GENERALに参加しているメンバー一覧
    users_format = users['members']

    users_name = []
    users_id = []

    for user_list in users_format:
        users_name.append(user_list['name'])
        users_id.append(user_list['_id'])
    
    users_dict = dict(zip(users_name, users_id))
    
    return users_dict

def find_group_user_id(channel_id):
    users = rocket.groups_members(room_id=channel_id).json() # GENERALに参加しているメンバー一覧
    users_format = users['members']

    users_name = []
    users_id = []

    for user_list in users_format:
        users_name.append(user_list['name'])
        users_id.append(user_list['_id'])
    
    users_dict = dict(zip(users_name, users_id))
    
    return users_dict

def find_dms():
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

    return dms_dict

def send_seers(seers):
    dms_dict = find_dms()
    print('占い師は' + seers + 'です。')
    rocket.chat_post_message('あなたは占い師です', room_id=dms_dict[seers])

def send_werewolfs(werewolfs):
    dms_dict = find_dms()
    users_dict = find_user_id('GENERAL')
    i = 0
    for werewolf in werewolfs:
        i = i + 1
        print('人狼' + str(i) + 'は' + werewolf + 'です。')
        rocket.chat_post_message('あなたは人狼です \n werewolf-chatとにて他の人狼と話し合いましょう!', room_id=dms_dict[werewolf])
        rocket.groups_invite('5GkWRnwiAsSJRsQ4g', users_dict[werewolf])

def send_villagers(villagers):
    dms_dict = find_dms()
    i = 0
    for villager in villagers:
        i = i + 1
        print('村人' + str(i) + 'は' + villager + 'です。')
        rocket.chat_post_message('あなたは村人です', room_id=dms_dict[villager])

def random_position():
    members_list = find_members()

    # 占い師を選出(1人)
    random_member = random.randrange(len(members_list)) - 1
    seers = members_list.pop(random_member)
    send_seers(seers)
    
    # 人狼を選出(2人)
    werewolfs = []
    for i in range(2):
        random_member = random.randrange(len(members_list)) - 1
        werewolfs.append(members_list.pop(random_member))
    send_werewolfs(werewolfs)

    # 残り全員を村人に選出
    send_villagers(members_list)

def remove_werewolfs(): # ゲーム終了時人狼チャットから全員追い出す
    users_id = find_group_user_id('5GkWRnwiAsSJRsQ4g') # 人狼チャットに参加しているメンバー全員を取得

    for user_id in users_id.values():
        if user_id != 'fyNf7LGr3Z9fzxaXY': # Werewolf以外の全てのユーザを追い出す
            rocket.groups_kick('5GkWRnwiAsSJRsQ4g', user_id)

def vote_time(start_time):
    rocket.chat_post_message('投票タイムが開始しました', channel='GENERAL')

    while True:
        end_time = time()
        if end_time - start_time >= 10: # 投票終了
            rocket.chat_post_message('投票タイムが終了しました', channel='GENERAL')
            return time()
    

def night_time(start_time):
    rocket.chat_post_message('夜の時間が開始しました', channel='GENERAL')
    
    while True:
        end_time = time()
        if end_time - start_time >= 10: # 夜の終了
            rocket.chat_post_message('夜の時間が終了しました', channel='GENERAL')
            start_time = time()
            return time()
    
