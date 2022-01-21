import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder-key-in-case-none-exists'