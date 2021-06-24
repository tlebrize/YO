class Settings:
    HOST = "http://localhost:8000"
    SECRET_KEY = "secr3t"
    DEBUG = True
    ORIGINS = [
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
        "https://yo.theof.fr",
    ]
    DB_URL = "postgres://yo:securepasswd@0.0.0.0:5432/yo"
