from time import sleep
from game import *

def run():

    while True:

        while True: # ゲームを開始するまでの処理
            message = get_message()

            if start_game(message) == 1:
                break

            sleep(1)

        while True: # ゲームを介した後の処理
            message = get_message()

            if stop_game(message) == 1:
                break

            compare_message(message)

            sleep(1)