import json
import os

from jif.helpers import load_jif_file, read_reqs_file, save_jif_file


def install_packages(args, kwargs, dev_requirements, requirements, jif_dict):
    for package in args:
        os.system(f"python -m pip install {package}")

        if kwargs.get("dev"):
            if package not in dev_requirements:
                jif_dict["dev_requirements"].append(package)
                save_jif_file(jif_dict)

        elif kwargs.get("save") not in [False, "false", "no"]:
            if package not in requirements:
                jif_dict["requirements"].append(package)
                save_jif_file(jif_dict)


def install(*args, **kwargs):
    jif_dict = load_jif_file()
    dev_requirements = jif_dict.get("dev_requirements", [])
    requirements = jif_dict.get("requirements", [])

    install_packages(args, kwargs, dev_requirements, requirements, jif_dict)
