
# jif
###### because I'm jealous of NPM.

---

## FAQ

### What is jif?
jif is a small CLI tool inspired by NPM and built on top of pip. There are no plans to make jif anything more. It is a small tool with a handful of commands that solve pain points I face on a daily basis.

### Why jif?
I frequently switch between Python and Node at work. I normally add a package.json to the Python projects simply to have a place to store my scripts. This works fine for development as I have NPM already installed locally. However, when deploying applications to a VM this becomes an issue since a machine spun up for a Python app doesn't have NPM installed.

TLDR - jif started out as a simple CLI tool built in Python to run scripts similar to npm (`npm run`).

### This sounds awesome, are there any limitations?
Yes, yes there are my friend. The biggest limitation is virtual environment management. Python's virtualenv is simple and works, jif has no intention of trying to replace or abstract it. I recommend using jif inside a virtualenv, that's what is was designed to do. You can use it globally just don't complain if something doesn't work like you expected it to. Or do and maybe I'll fix it.

If you run into any other limitations or bugs feel free to create an issue.

---

## Installation
`python -m pip install jif`
*As stated above, I recommend using jif within a virtualenv

## Commands

You can view all the commands with the CLI by running `jif --help`.
If you want more details about a specific command, run `jif <COMMAND> --help`. 

1) `init`
2) `run`
3) `install`
4) `uninstall`
5) `freeze`


### `init`
The `init` command creates the jif file (`jif.json`) that the other commands use. The file will be saved in the dir that the command is run.

##### Optional flags
1) `--entry-point`: use this flag to point to the module that should run when calling the start command.
        - Default: `app.py`
> 
2) `--lint-dir`: use this flag to tell jif which directory should be linted.
        - Default: `.`
>
3) `--reqs`: location of your requirements file.
        - Set reqs to 'inline' if you want your dependecies managed in the jif.json (jif init --reqs inline)
        - Default: `requirements.txt`
>
4) `--dev-reqs`: location of your dev requirements file.
        - Set dev reqs to 'inline' if you want your dependecies managed in the jif.json (jif init --dev-reqs inline)
        - Default: `dev_requirements.txt`
>
5) `--author`: credits author.
        - Default: None, omitted unless value is specified.
>
6) `--version`: which version your package is at.
        - Default: `0.0.1`
>
7) `--package-name`: name of your package.
        - Default: None, omitted unless value is specified.

_examples_: `jif init`, `jif init --lint-dir src --entry-point src/

### `run`
The jif file let's you store scripts which can be executed using the `run` command. There are 3 script names that can omit the `run` keyword:
1. `start`
2. `lint`
3. `test`

_examples_: `jif start`, `jif run my_script`

### `freeze`
The `freeze` command literally just calls `pip freeze > requirements.txt`. There are no flags, no customization, just a simple command I use occasionally that saves me a fraction of a second

_examples_: `jif freeze`, `jif f`