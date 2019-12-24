import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="jif",
    version="0.0.8",
    description="CLI tool to run scipts",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JasonAtallah/jif",
    download_url="https://github.com/JasonAtallah/jif/archive/v0.0.8.tar.gz",
    author="Jason Atallah",
    author_email="jason.atallah@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["jif", "jif.commands"],
    include_package_data=True,
    install_requires=["black", "fire"],
    extras_require={"dev": ["portray"]},
    entry_points={"console_scripts": ["jif=jif.__main__:main",]},
)
