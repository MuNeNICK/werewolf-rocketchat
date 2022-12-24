import os
from requests import sessions
from rocketchat_API.rocketchat import RocketChat


username = "BOT2"
password = os.environ.get('ROCKET_PASSWORD')
server_url = os.environ.get('ROCKET_SERVER_URL')

with sessions.Session() as session:
    bot2_rocket = RocketChat(username, password, server_url=server_url, session=session)
