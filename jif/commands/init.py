import json


def create_json_data(kwargs):
    requirements = kwargs.get("reqs", "requirements.txt")
    dev_requirements = kwargs.get("dev_reqs", "dev_requirements.txt")
    entry_point = kwargs.get("entry_point", "app.py")

    return {
        "scripts": {
            "start": f"python {entry_point}",
            "lint": "black .",
            "test": "python -m unittest discover",
        },
        "requirements": requirements,
        "dev_requirements": dev_requirements,
    }


def init(**kwargs):
    default_jif = create_json_data(kwargs)

    with open("jif.json", "w") as json_file:
        json.dump(default_jif, json_file, indent=4)
