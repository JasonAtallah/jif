import argparse
import json
import logging
import os
import sys
import yaml

logger_format = "[%(name)s.%(levelname)s] %(message)s"
logger_level = int(os.environ.get("LOGGER_LEVEL", 20))
logging.basicConfig(format=logger_format, level=logger_level)
logger = logging.getLogger("jif")


def get_script(script_name, scripts):
    """
    Gets script by script name from scripts dict.
    If script cannot be found, will throw an error and end execution.
    """
    try:
        script = scripts[script_name]
        logger.debug(f"script: {script}")
        return script
    except KeyError as _:
        logger.error(f"Script does not exist: {script_name}")
        sys.exit()


def get_scripts(jif_file):
    """
    Gets all scripts from the jif file.
    If no scripts object exists, will throw an error and end execution.
    """
    try:
        scripts = jif_file.get("scripts")
        logger.debug(f"scripts: {scripts}")
        return scripts
    except KeyError as _:
        logger.error("Jif file is missing the 'scripts' object")
        sys.exit()


def get_script_name(res):
    """
    Gets the script name from the commands args.
    If no args were passed in, will throw an error and end execution. 
    """
    try:
        script_name = res.script_name
        logger.debug(f"script_name: {script_name}")
        return script_name
    except AttributeError as _:
        logger.error("Script name is required")
        sys.exit()


def load_jif_file():
    """
    Loads jif file in current directory.
    If file doesn't exist, will throw an error and end execution.
    """
    try:
        jif_file = json.load(open("jif.json"))
        logger.debug(f"jif_file: {jif_file}")
        return jif_file
    except FileNotFoundError as _:
        try:
            jif_file = yaml.safe_load(open("jif.yml"))
            logger.debug(f"jif_file: {jif_file}")
            return jif_file
        except FileNotFoundError as _:
            logger.error("Directory does not contain jif.json or jif.yml")
            sys.exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("script_name", help="script name")
    res = parser.parse_args()
    logger.debug(f"res: {res}")

    script_name = get_script_name(res)
    jif_file = load_jif_file()
    scripts = get_scripts(jif_file)
    script = get_script(script_name, scripts)

    os.system(script)


if __name__ == "__main__":
    main()
