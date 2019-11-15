import os


def write_to_file(filename, package):
    with open(filename, "a") as f:
        f.write(f"{package}\n")


def install(self, *args, **kwargs):
    '''
    install command for jif
    '''
    for package in args:
        os.system(f"python -m pip install {package}")

        is_dev = kwargs.get("dev", False)
        is_save = kwargs.get("save", False)
        if is_dev:
            dev_filename = "dev_requirements.txt" if is_dev == True else is_dev
            write_to_file(dev_filename, package)
        elif is_save:
            filename = "requirements.txt" if is_save == True else is_save
            write_to_file(filename, package)
        else:
            write_to_file("requirements.txt", package)
