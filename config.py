import os

class Config(object):
    SECRET_KEY = os.envrion.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }