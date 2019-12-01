import json
import os

from jif.helpers import load_jif_file, read_reqs_file, save_jif_file


def install_package(package):
    os.system(f"python -m pip install {package}")


def install(*args, **kwargs):
    jif_dict = load_jif_file()
    new_jif_dict = jif_dict.copy()
    dev_requirements = jif_dict.get("dev_requirements", [])
    requirements = jif_dict.get("requirements", [])
    shoulds_save = kwargs.get("save") not in [False, "false", "no"]

    if args:
        for package in args:
            install_package(package)

            if kwargs.get("dev") and package not in dev_requirements:
                dev_requirements.append(package)
                new_jif_dict["dev_requirements"] = dev_requirements

            if shoulds_save and package not in requirements:
                requirements.append(package)
                new_jif_dict["requirements"] = requirements
    else:
        for package in dev_requirements:
            install_package(package)
        for package in requirements:
            install_package(package)

    save_jif_file(new_jif_dict)
