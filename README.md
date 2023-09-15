# Overview

I'm just setting up a new VS Code environment for Python and getting all the settings right.

- .vscode folder contains settings for the IDE
- hello.py defines a simple Hello class and console application
- hello_test.py runs a unit test using the `pytest` module
- requirements.txt is a list of packages installed in my virtual environment
- README.md is this file

{Provide a link to your YouTube demonstration.  It should be a one minute demo of the software running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

My environment VS Code with the following extensions installed:

- MyPy - Python type-checker from Microsoft
- Pylint - Linting support for python
- Python - Microsoft's language, formatting, and Intellisense extension
- Python Resource Monitor - Shows memory usage when debugging
- Python Test Explorer for VS Code - finds and runs the unit tests

The code is written with Python, an interpreted, object-oriented, high-level
programming language with dynamic semantics.

> NOTE: If you choose to use a dedicated Python virtual environment (.venv),
  you can use `requirements.txt`` to install packages.

```python
pip install -r requirements.txt
```

# Useful Websites

* [W3School Python Tutorial](https://www.w3schools.com/python/default.asp) for a
  quick refresher of Python syntax.

* [typing - Support for type hints](https://docs.python.org/3/library/typing.html)
  for Python syntax to support strongly typed arguments and return values.

* [pytest Documentation](https://docs.pytest.org/en/7.1.x/index.html) for examples
  of unit tests written for `pytest`.