[![PyPI version](https://badge.fury.io/py/jif.svg)](https://badge.fury.io/py/jif)

# jif

jif is a small CLI tool to store and run bash scripts. Inspired by `npm run`.

## Usage

1. Create a jif file (`jif.json` or `jif.yml`).
2. Add a scripts object. E.g. 
```
{
    "scripts": {
        "start": "python app.py",
        "lint": "black myapp"
    }
}
```

or

```
scripts:
  start: python app.py
  lint: black myapp
```

3. Use jif to run your scripts. E.g. `jif start`, `jif lint`

4. Profit???