import os


class Settings:
    HOST = os.environ.get("HOST", "http://localhost:8000")
    SECRET_KEY = os.environ.get("SECRET_KEY", "secr3t")
    DEBUG = os.environ.get("DEBUG", "True") == "True"
