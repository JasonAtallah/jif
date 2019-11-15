import os

# WIP
def uninstall(*args):
    for package in args:
        os.system(f"python -m pip uninstall {package}")
