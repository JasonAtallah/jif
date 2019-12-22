import json
import logging
import sys
from typing import Any, Dict

logger = logging.getLogger("jif")


def load_jif_file() -> None:
    """
    Loads jif file in current directory.
    If file doesn't exist, will throw an error and end execution.
    """
    try:
        jif_file = json.load(open("jif.json"))
        return jif_file
    except FileNotFoundError as _:
        logger.error("directory does not contain jif.json")
        logger.info("run 'jif init' to create a jif.json")
        sys.exit()


def read_reqs_file(filename: str) -> str:
    """
    Finds, opens and returns file.

    Args
        filename (str): name of file you want to retrieve.

    Returns
        reqs_file (Any): opens and returns contents of file.
    """
    with open(filename, "r") as reqs_file:
        return reqs_file


def save_jif_file(jif_dict: Dict[str, Any]) -> None:
    """
    Updates jif file with dict passed in.

    Args
        jif_dict (Dict): used to overwrite jif file.

    Returns
        None
    """
    with open("jif.json", "w") as json_file:
        json.dump(jif_dict, json_file, indent=4)


def update_requirements_file(requirements_file: str, requirements: str) -> None:
    """
    Args
        requirements_file (str) name of file to be updated
        requirements (str) stringified list of requirements
    """
    if requirements_file:
        reqs_string = ""
        for req in requirements:
            reqs_string += f"{req}\n"

        if reqs_string:
            with open(requirements_file, "w") as f:
                f.write(reqs_string)
