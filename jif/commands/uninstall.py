import logging
import os

from jif.helpers import load_jif_file, save_jif_file, update_requirements_file

logger = logging.getLogger("jif")


def uninstall_package(package: str) -> None:
    try:
        os.system(f"python -m pip uninstall {package} -y")
    except Exception as e:
        logger.error(f"{e}\nFailed to uninstall package {package}")


def uninstall(*args, **kwargs):
    """
    Uninstalls packages (run 'jif uninstall --help' for more details)
    """
    if kwargs.get("help"):
        uninstall_help()
        return

    jif_dict = load_jif_file()
    new_jif_dict = jif_dict.copy()
    dev_requirements = jif_dict.get("dev_requirements", [])
    dev_requirements_file = jif_dict.get("dev_requirements_file")
    requirements = jif_dict.get("requirements", [])
    requirements_file = jif_dict.get("requirements_file")

    for package in args:
        uninstall_package(package)
        if package in dev_requirements:
            dev_requirements.remove(package)
            new_jif_dict["dev_requirements"] = dev_requirements
            update_requirements_file(dev_requirements_file, dev_requirements)

        if package in requirements:
            requirements.remove(package)
            new_jif_dict["requirements"] = requirements
            update_requirements_file(requirements_file, requirements)

    save_jif_file(new_jif_dict)


def uninstall_help():
    logger.info(
        """
        \n
        The `uninstall` command will uninstall all packages specified then check to see if they are listed in either the requirements or dev requirements in the jif file. If they are in either, they will be removed.

        Examples
            jif uninstall black autopep8 flask
        \n
        """
    )
