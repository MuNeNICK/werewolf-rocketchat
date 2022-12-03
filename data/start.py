from time import sleep
from game import *

def run():
    start_game()

    send_position()

    while True:
        message = get_message()
        stop_game(message)
        compare_message(message)

        sleep(1)