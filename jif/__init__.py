import fire
import json
import logging
import os

from jif.commands.init import init
from jif.commands.install import install
from jif.commands.run import run, lint, start, test
from jif.commands.uninstall import uninstall

logger_format = "[%(name)s.%(levelname)s] %(message)s"
logging.basicConfig(format=logger_format, level=1)


def main():
    fire.Fire()
