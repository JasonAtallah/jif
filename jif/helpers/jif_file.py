import json
import logging
import sys

logger = logging.getLogger("jif")


def load_jif_file():
    try:
        jif_file = json.load(open("jif.json"))
        return jif_file
    except FileNotFoundError as _:
        logger.error("directory does not contain jif.json")
        logger.info("run 'jif init' to create a jif.json")
        sys.exit()
