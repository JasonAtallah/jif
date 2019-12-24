import fire
import logging

from jif.commands.init import init
from jif.commands.install import install
from jif.commands.run import lint, run, start, test
from jif.commands.uninstall import uninstall
from jif.commands.version import version

logger_format = "[%(name)s.%(levelname)s] %(message)s"
logging.basicConfig(format=logger_format, level=1)


def main():
    fire.Fire(
        {
            "init": init,
            "install": install,
            "i": install,
            "lint": lint,
            "run": run,
            "start": start,
            "test": test,
            "uninstall": uninstall,
            "version": version
        }
    )


if __name__ == "__main__":
    main()
