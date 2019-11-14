import fire
import json
import logging
import os


class Jif:
    jif_file = json.load(open("jif.json"))

    def run(self, script_name):
        script = self.jif_file["scripts"].get(script_name, False)

        if script:
            os.system(script)
        else:
            logging.error(f"{script_name} script doesn't exist")
            

def main():
    fire.Fire(Jif)


if __name__ == "__main__":
    main()
