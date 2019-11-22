import json

from jif.helpers import save_jif_file


def gen_dev_requirements(kwargs):
    dev_reqs = kwargs.get("dev_reqs", "dev_requirements.txt")

    if dev_reqs == "inline":
        return []
    return dev_reqs


def gen_requirements(kwargs):
    reqs = kwargs.get("reqs", "requirements.txt")

    if reqs == "inline":
        return []
    return reqs


def create_jif_dict(kwargs):
    author = kwargs.get("author", False)
    entry_point = kwargs.get("entry_point", "app.py")
    lint_dir = kwargs.get("lint_dir", ".")
    package_name = kwargs.get("package_name", False)
    version = kwargs.get("version", "0.0.1")

    jif_dict = {
        "version": version,
        "scripts": {
            "start": f"python {entry_point}",
            "lint": f"black {lint_dir}",
            "test": "python -m unittest discover",
        },
        "requirements": gen_requirements(kwargs),
        "dev_requirements": gen_dev_requirements(kwargs),
    }

    if author:
        jif_dict["author"] = author

    if package_name:
        jif_dict["package_name"] = package_name

    return jif_dict


def init(**kwargs):
    jif_dict = create_jif_dict(kwargs)
    save_jif_file(jif_dict)
