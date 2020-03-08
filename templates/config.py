from os import environ
import os

class Config:
    SECRET_KEY = #PUT SECRET KEY HERE
    TESTING = False
    DEBUG = True
    SESSION_TYPE = environ.get('SESSION_TYPE')


