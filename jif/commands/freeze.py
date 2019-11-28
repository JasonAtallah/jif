import os


def freeze(**kwargs):
    os.system("pip freeze > requirements.txt")
