import os


class Config:
    SECRET_KEY = os.environ.get("SECRETKEY") or "you-will-never-guess"
