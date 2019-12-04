import logging
import os

from jif.helpers import load_jif_file

logger = logging.getLogger("jif")


def start():
    """
    Runs start script
    """
    run("start")


def test():
    """
    Runs test script
    """
    run("test")


def lint():
    """
    Runs lint script
    """
    run("lint")


def run(script_name=None, **kwargs):
    """
    \n
    Runs script in jif file (run 'jif run --help' for more details)
    \n
    """
    if kwargs.get("help"):
        run_help()
        return

    jif_file = load_jif_file()
    scripts = jif_file.get("scripts")

    if not script_name:
        for script in scripts:
            print("\n", script + ":", scripts[script])
        print("\n")
        return

    script = scripts.get(script_name)

    if script:
        os.system(script)
    else:
        logger.error(f"script does not exist: {script_name}")


def run_help():
    logger.info(
        """
        \n
        The jif file let's you store scripts which can be executed using the run command. There are 3 script names that can omit the run keyword:
        1. start
        2. lint
        3. test
        \n

        Examples
            jif start
            jif run my_script
        \n
        """
    )
