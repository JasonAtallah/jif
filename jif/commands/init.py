import json
import logging
from typing import Any, Dict

from jif.helpers import save_jif_file

logger = logging.getLogger("jif")


def create_jif_dict(kwargs) -> Dict[str, Any]:
    """
    Parses flags and builds dict that will be used to create the jif.json

    Args
        kwargs (Dict): contains flags passed into the init command.

    Returns
        jif_dict (Dict): dict used to create jif.json.
    """
    entry_point = kwargs.get("entry_point", "app.py")
    lint_dir = kwargs.get("lint_dir", ".")

    author = kwargs.get("author", False)
    package_name = kwargs.get("package_name", False)
    version = kwargs.get("version", "0.0.1")

    jif_dict = {
        "version": version,
        "scripts": {
            "start": f"python {entry_point}",
            "lint": f"black {lint_dir}",
            "test": "python -m unittest discover",
        },
        "requirements": [],
        "dev_requirements": [],
        "requirements_file": "requirements.txt",
        "dev_requirements_file": "dev_requirements.txt",
    }

    if author:
        jif_dict["author"] = author

    if package_name:
        jif_dict["package_name"] = package_name

    return jif_dict


def init(**kwargs):
    """
    Initializes jif file (run 'jif init --help' for more details)
    """
    if kwargs.get("help"):
        init_help()
        return

    jif_dict = create_jif_dict(kwargs)
    save_jif_file(jif_dict)


def init_help():
    logger.info(
        """
        \n
        "init" command is used for creating a jif.json.\n

        Optional flags
            1) --entry-point: use this flag to point to the module that should run when calling the start command.
            - Default: app.py

            2) --lint-dir: use this flag to tell jif which directory should be linted.
            - Default: .

            3) --author: credits author.
            - Default: None, omitted unless value is specified.

            4) --version: which version your package is at.
            - Default: 0.0.1

            5) --package-name: name of your package.
            - Default: None, omitted unless value is specified.

        Examples
            jif init
            jif init --lint-dir src --entry-point src/main.py
        \n
        """
    )
