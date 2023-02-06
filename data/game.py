import random
from time import sleep,time
from pprint import pprint
from main import rocket
from agents.bot1.bot1_ai import *
from agents.bot2.bot2_ai import *
from agents.bot3.bot3_ai import *
from agents.bot4.bot4_ai import *
from agents.bot5.bot5_ai import *
from agents.bot6.bot6_ai import *

def start_game(message, day):
    if message == '!start':
        rocket.chat_post_message('人狼ゲームを始めます', channel='GENERAL')
        revive()
        random_position()

        say_day(day)

        bot1_intro()
        bot2_intro()
        bot3_intro()
        bot4_intro()
        bot5_intro()
        bot6_intro()

        return 1

def stop_game(message):
    if message == '!stop':
        rocket.chat_post_message('人狼ゲームを終了します', channel='GENERAL')
        remove_werewolfs()
        return 1

def get_message(): # 最新のメッセージを取得
    message = rocket.channels_history('GENERAL',count=1).json() # dict型 GENERALの最新メッセージを取得
    message_format = message['messages'] # list型
    if not message_format: # メッセージがない場合
        message_split = 'empty_message' # 空のメッセージを返す
    else:
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
        users_name.append(user_list['username'])
        users_id.append(user_list['_id'])
    
    users_dict = dict(zip(users_name, users_id))
    
    return users_dict

def find_group_user_id(channel_id):
    users = rocket.groups_members(room_id=channel_id).json() # GENERALに参加しているメンバー一覧
    users_format = users['members']

    users_name = []
    users_id = []

    for user_list in users_format:
        users_name.append(user_list['username'])
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
        for dm_user in dm_users:
            if dm_user != 'Werewolf':
                dms_users_list.append(dm_user)

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
        rocket.chat_post_message('あなたは人狼です \n #werewolf-chatとにて他の人狼と話し合いましょう!', room_id=dms_dict[werewolf])
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
    at_strings = []

    while True:
        bot1_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)
            
        bot2_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)
            
        bot3_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)

        bot4_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)

        bot5_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)
            
        bot6_vote()
        vote_result = vote()
        if vote_result != None:
            at_strings.append(vote_result)
                
        end_time = time()

        if end_time - start_time >= 30: # 投票終了
            vote_target = most_common_element(at_strings)
            rocket.chat_post_message(vote_target + "が追放されます。", channel='GENERAL')
            dead(vote_target)
            rocket.chat_post_message('投票タイムが終了しました', channel='GENERAL')
            return time()

def most_common_element(arr):
    # 各要素の出現回数を数えます
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # 出現回数が最大の要素を取得します
    max_element = None
    max_count = 0
    for i in count:
        if count[i] > max_count:
            max_element = i
            max_count = count[i]
    return max_element

def night_time(start_time):
    rocket.chat_post_message('夜の時間が開始しました', channel='GENERAL')
    while True:
        end_time = time()
        if end_time - start_time >= 30: # 夜の終了
            rocket.chat_post_message('夜の時間が終了しました', channel='GENERAL')
            start_time = time()
            return time()

def dead(name):
    name_after = name.lstrip('@')
    rocket.roles_remove_user_from_role('Alive', name_after)
    rocket.roles_add_user_to_role('Dead', name_after)

def revive():
    members = find_members()
    for member in members:
        rocket.roles_remove_user_from_role('Dead', member)
        rocket.roles_add_user_to_role('Alive', member)
    
def vote():
    message = get_message()
    if '!vote' in message:
        for word in message.split():
            if word.startswith('@'):
                at_strings = word
        rocket.chat_post_message(at_strings + 'に投票しました', channel='GENERAL')
        return at_strings

def talk_time():
    message = get_message()
    bot1_response(message)

    # message = get_message()
    # bot2_response(message)

    # message = get_message()
    # bot3_response(message)

    # message = get_message()
    # bot4_response(message)

    # message = get_message()
    # bot5_response(message)

    # message = get_message()
    # bot6_response(message)

def say_day(day):
    rocket.chat_post_message(str(day) + '日目の朝です', channel='GENERAL')

def day_count(day):
    day = day + 1

    say_day(day)
    return day
