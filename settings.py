import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')
invalid_email =os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')
valid_tel = os.getenv('valid_tel')
invalid_tel = os.getenv('invalid_tel')
valid_lc = os.getenv('valid_lc')
valid_login = os.getenv('valid_login')
invalid_lc = os.getenv('invalid_lc')
invalid_login = os.getenv('invalid_login')
