import os
from requests import sessions
from rocketchat_API.rocketchat import RocketChat


username = "BOT4"
password = os.environ.get('ROCKET_PASSWORD')
server_url = os.environ.get('ROCKET_SERVER_URL')

with sessions.Session() as session:
    bot4_rocket = RocketChat(username, password, server_url=server_url, session=session)
