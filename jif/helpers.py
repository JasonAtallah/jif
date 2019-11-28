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


def read_reqs_file(filename):
    """
    Finds, opens and returns file.

    Args
        filename (str): name of file you want to retrieve.

    Returns
        reqs_file (Any): opens and returns contents of file.
    """
    with open(filename, "r") as reqs_file:
        return reqs_file


def save_jif_file(jif_dict):
    """
    Updates jif file with dict passed in.

    Args
        jif_dict (Dict): used to overwrite jif file.

    Returns
        None
    """
    with open("jif.json", "w") as json_file:
        json.dump(jif_dict, json_file, indent=4)
