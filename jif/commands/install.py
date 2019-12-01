import json
import logging
import os

from jif.helpers import load_jif_file, save_jif_file

logger = logging.getLogger("jif")


def install_package(package):
    os.system(f"python -m pip install {package}")


def install(*args, **kwargs):
    """
    Installs packages (Run 'jif install --help' for more details)
    """

    if kwargs.get("help"):
        install_help()
        return

    jif_dict = load_jif_file()
    new_jif_dict = jif_dict.copy()
    dev_requirements = jif_dict.get("dev_requirements", [])
    requirements = jif_dict.get("requirements", [])

    if args:
        for package in args:
            install_package(package)

            if kwargs.get("dev") and package not in dev_requirements:
                dev_requirements.append(package)
                new_jif_dict["dev_requirements"] = dev_requirements

            elif not kwargs.get("no_save") and package not in requirements:
                requirements.append(package)
                new_jif_dict["requirements"] = requirements
    else:
        for package in dev_requirements:
            install_package(package)
        for package in requirements:
            install_package(package)

    save_jif_file(new_jif_dict)


def install_help():
    logger.info(
        """
        \n
        The "install" command uses pip to install packages and then automatically manages them for you in your jif file.

        Optional flags
            1) --dev: Add this flag to the end of your command to save all packages as dev requirements.
            2) --no-save: Add this flag to the end of your command to only install packages locally and not have them managed in the jif file.

        Examples
            jif install flask
            jif install black autopep8 --dev
            jif install black --no-save
        \n
        """
    )
