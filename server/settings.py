class Settings:
    HOST = "http://localhost:8000"
    SECRET_KEY = "secr3t"
    DEBUG = True
    ORIGINS = [
        "http://localhost:8000/",
        "http://localhost:8080/",
    ]
    DB_URL = "postgres://yo:securepasswd@0.0.0.0:5432/yo"
