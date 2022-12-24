import os
from requests import sessions
from rocketchat_API.rocketchat import RocketChat

from . import bot1_ai

def start_bot1():
    username = "BOT1"
    password = os.environ.get('ROCKET_PASSWORD')
    server_url = os.environ.get('ROCKET_SERVER_URL')

    with sessions.Session() as session:
        rocket = RocketChat(username, password, server_url=server_url, session=session)

        rocket.chat_post_message('BOT1です', channel='GENERAL')

    response = bot1_ai.handle_response("世界で一番人口が多い国は？")
    rocket.chat_post_message(response, channel='GENERAL')
