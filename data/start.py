from time import sleep,time
from game import *
from agents.bot1.bot1 import *


def run():
    rocket.chat_post_message('!start', channel='GENERAL')

    day = 1

    while True:

        while True: # ゲームを開始するまでの処理
            message = get_message()

            if start_game(message, day) == 1:
                start_time = time() # 議論のカウントスタート
                break

            sleep(1)

        while True: # ゲームを開始した後の処理
            end_time = time()
        
            message = get_message()

            compare_message(message)

            talk_time()

            if stop_game(message) == 1:
                break

            if end_time - start_time >= 10: # 投票開始の処理
                start_time = vote_time(time()) # 投票の開始

                start_time = night_time(time()) # 夜の開始

                day = day_count(day)

            sleep(1)
