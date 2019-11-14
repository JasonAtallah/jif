import logging
import os

from jif.jif_file import jif_file

logger = logging.getLogger("jif")


def start(self):
    run("start")


def test(self):
    run("test")


def lint(self):
    run("lint")


def run(self, script_name):
    script = jif_file["scripts"].get(script_name, False)

    if script:
        os.system(script)
    else:
        logger.error(f"script does not exist: {script_name}")
