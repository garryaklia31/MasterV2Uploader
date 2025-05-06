import os

class Config(object):
    BOT_TOKEN = os.environ.get("8146719460:AAGwfW09HZ1j94OY3M-4BzHrcJysJsgpbS0")
    API_ID = int(os.environ.get("22182189"))
    API_HASH = os.environ.get("5e7c4088f8e23d0ab61e29ae11960bf5")
    VIP_USER = os.environ.get('VIP_USERS', '1718738592').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]
