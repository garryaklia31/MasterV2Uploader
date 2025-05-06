from os import environ

API_ID = int(environ.get("API_ID", "22182189"))
API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = environ.get("BOT_TOKEN", "8146719460:AAGwfW09HZ1j94OY3M-4BzHrcJysJsgpbS0")
VIP_USER = environ.get('VIP_USERS', '1718738592').split(',')
VIP_USERS = [int() for user_id in VIP_USER]
