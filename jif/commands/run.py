import logging
import os

from jif.helpers import load_jif_file

logger = logging.getLogger("jif")


def start():
    run("start")


def test():
    run("test")


def lint():
    run("lint")


def run(script_name):
    jif_file = load_jif_file()
    script = jif_file["scripts"].get(script_name, False)

    if script:
        os.system(script)
    else:
        logger.error(f"script does not exist: {script_name}")
