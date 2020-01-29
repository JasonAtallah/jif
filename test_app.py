import os

env = os.environ.get('ENVIRONMENT')
print(env.get('envname'))