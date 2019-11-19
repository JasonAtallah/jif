import json
import os

from jif.helpers.jif_file import load_jif_file, save_jif_file


def file_has_string(filename, string):
    with open(filename) as f:
        return string in f


def write_to_file(filename, package):
    with open(filename, "a") as f:
        f.write(f"{package}\n")


def install(*args, **kwargs):
    jif_dict = load_jif_file()
    dev_requirements = jif_dict.get("dev_requirements", "dev_requirements.txt")
    requirements = jif_dict.get("requirements", "requirements.txt")

    for package in args:
        os.system(f"python -m pip install {package}")

        if kwargs.get("dev"):
            if type(dev_requirements) == list and package not in dev_requirements:
                jif_dict["dev_requirements"].append(package)
                save_jif_file(jif_dict)

            elif not file_has_string(dev_requirements, package):
                write_to_file(dev_requirements, package)

        elif kwargs.get("save"):
            if type(requirements) == list and package not in requirements:
                jif_dict["requirements"].append(package)
                save_jif_file(jif_dict)
            elif not file_has_string(requirements, package):
                write_to_file(requirements, package)
