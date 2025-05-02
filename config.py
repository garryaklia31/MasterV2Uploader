import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get(""))
    API_HASH = os.environ.get("")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]
