import os
from requests import sessions
from rocketchat_API.rocketchat import RocketChat

def start_bot1():
    username = "BOT1"
    password = os.environ.get('ROCKET_PASSWORD')
    server_url = os.environ.get('ROCKET_SERVER_URL')

    with sessions.Session() as session:
        rocket = RocketChat(username, password, server_url=server_url, session=session)

        rocket.chat_post_message('BOT1です', channel='GENERAL')

