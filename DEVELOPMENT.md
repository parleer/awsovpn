

# Development

Regenerate requirements.txt form requirements.in

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

Install the package in 'edit' mode. Now you can invoke the package using the name `word` as defined by `setup.py`.

```bash
pip install -e .
```


### Build

```bash
# Normal build
python -m pip install --upgrade setuptools build
python -m build
```

### Publish to Test PyPI

https://twine.readthedocs.io/en/stable/

```bash
python -m pip install --upgrade twine
python -m twine upload --verbose -r testpypi dist/*
```


### Test from test.pypi.org

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/  awsovpn
```


### Publish to PyPI

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

### Run from PyPi.org

```bash
python -m pip install awsovn
```
