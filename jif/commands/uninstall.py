import os

# WIP
def uninstall(*args):
    """
    Work in progress. Currently doesn't remove packages from requirements file or array.
    """
    for package in args:
        os.system(f"python -m pip uninstall {package}")
