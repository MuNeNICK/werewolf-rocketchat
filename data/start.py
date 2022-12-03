from time import sleep
from game import *

def run():
    while 1:
        message = get_message()
        compare_message(message)
        sleep(1)