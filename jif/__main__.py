import fire
import json
import logging
import os

logger_format = "[%(name)s.%(levelname)s] %(message)s"
logging.basicConfig(format=logger_format, level=1)
logger = logging.getLogger("jif")


class Jif:
    jif_file = json.load(open("jif.json"))

    def start(self):
        self.run("start")

    def test(self):
        self.run("test")

    def lint(self):
        self.run("lint")

    def run(self, script_name):
        script = self.jif_file["scripts"].get(script_name, False)

        if script:
            os.system(script)
        else:
            logger.error(f"script does not exist: {script_name}")

    def install(self, *args, **kwargs):
        for package in args:
            os.system(f"python -m pip install {package}")

            is_dev = kwargs.get("dev", False)
            is_save = kwargs.get("save", False)
            if is_dev:
                dev_filename = "dev_requirements.txt" if is_dev == True else is_dev
                self.write_to_file(dev_filename, package)
            elif is_save:
                filename = "requirements.txt" if is_save == True else is_save
                self.write_to_file(filename, package)
            else:
                self.write_to_file("requirements.txt", package)

    def uninstall(self, *args, **kwargs):
        for package in args:
            os.system(f"python -m pip uninstall {package}")

    @staticmethod
    def write_to_file(filename, package):
        with open(filename, "a") as f:
            f.write(f"{package}\n")


def main():
    fire.Fire(Jif)


if __name__ == "__main__":
    main()
