import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="jif",
    version="0.0.1",
    description="CLI tool to run scipts",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JasonAtallah/jif",
    author="Jason Atallah",
    author_email="jason.atallah@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["jif", "jif.commands", "jif.helpers"],
    include_package_data=True,
    install_requires=["black", "fire"],
    entry_points={"console_scripts": ["jif=jif.__main__:main",]},
)
