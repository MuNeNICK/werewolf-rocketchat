from rocketchat.api import RocketChatAPI

api = RocketChatAPI(settings={'username': 'Werewolf', 'password': 'Me1onpan#',
                              'domain': 'http://rocketchat:3000'})
                            
api.get_room_history('general')