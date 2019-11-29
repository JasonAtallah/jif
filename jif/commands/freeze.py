import logging
import os


logger = logging.getLogger("jif")


def freeze(**kwargs):
    """
    The freeze command just runs 'pip freeze > requirements.txt'.
    Nothing more, nothing less.
    'f' is also a shorthand for freeze
    """
    if kwargs.get("help"):
        freeze_help()
        return

    os.system("pip freeze > requirements.txt")


def freeze_help():
    logger.info(
        """
    \n
    The freeze command just runs 'pip freeze > requirements.txt'.
    Nothing more, nothing less.
    'f' is also a shorthand for freeze
    \n
    """
    )
