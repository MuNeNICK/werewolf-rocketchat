import os
from pyrocketbot import RocketBot

username = os.environ.get('ROCKET_USERNAME')
password = os.environ.get('ROCKET_PASSWORD')
server_url = os.environ.get('ROCKET_SERVER_URL')

proxy_dict = {
    "http"  : "http://127.0.0.1:2080",
    "https" : "https://127.0.0.1:2080",
}

# bot = RocketBot(username, password, server_url)
bot = RocketBot('Werewolf', 'Me1onpan#', server_url='http://rocketchat:3000')
# bot = RocketBot(username, password, server_url, proxy_dict=proxy_dict)


@bot.command(r'/start')
def start(message, match_list):
    # bot.send_message(message['rid'], 'hi')
    bot.send_message('general', 'hi')

@bot.command(r'/echo (.*)')
def echo(message, match_list):
    bot.send_message(message['rid'], match_list[0])


if __name__ == '__main__':
    print('Bot started')
    bot.run(chat_type='c', sleep=0.5)