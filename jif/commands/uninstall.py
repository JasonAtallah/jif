import os

from jif.helpers import load_jif_file, save_jif_file


def uninstall_package(package):
    os.system(f"python -m pip uninstall {package}")


def uninstall(*args, **kwargs):
    jif_dict = load_jif_file()
    new_jif_dict = jif_dict.copy()
    dev_requirements = jif_dict.get("dev_requirements", [])
    requirements = jif_dict.get("requirements", [])

    for package in args:
        uninstall_package(package)
        if package in dev_requirements:
            dev_requirements.remove(package)
            new_jif_dict["dev_requirements"] = dev_requirements

        if package in requirements:
            requirements.remove(package)
            new_jif_dict["requirements"] = requirements

    save_jif_file(new_jif_dict)
