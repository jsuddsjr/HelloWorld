# Overview

I'm just setting up a new VS Code environment for Python and getting all the settings right.
This project includes both unit tests and localization features for Python. The program currently
has translations for English (en_US), French (fr_FR), and German (de_DE).

## Setting your preferred language

You can easily switch between languages by setting the LANG environment variable to one of the ll_CC codes above.

```
set LANG=de_DE
```

Then run the `hello.py` file with the Python interpreter.

```
python src/hello.py

Hallo Welt!
```

{Provide a link to your YouTube demonstration.  It should be a one minute demo of the software running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

My environment VS Code with the following extensions installed:

- MyPy - Python type-checker from Microsoft
- Pylint - Linting support for python
- Python - Microsoft's language, formatting, and Intellisense extension

The code is written with Python, an interpreted, object-oriented, high-level
programming language with dynamic semantics.

> NOTE: If you choose to use a dedicated Python virtual environment (.venv),
  you can use `requirements.txt`` to install packages.

## Project structure

- .vscode
  - extensions.json &mdash; Recommended extensions for the project
  - launch.json &mdash; Debugger configuration to step through library code
  - settings.json &mdash; Workspace configuration for Python tools
- locale
  - ... &mdash; Folders containing .PO and .MO files for localized strings.
- src
  - hello_test.py &mdash; Unit tests
  - hello.py &mdash; An object-oriented implementation of Hello World.
- requirements.txt &mdash; Packages used by the virtual environment.
- README.md &mdash; This file.

## Setting up your virtual environment

1. Open the Command Palette (CTRL+SHIFT+P)
1. Select "Python: Create Environment"
1. Choose Venv option.
1. Choose a Python 3 engine (installed separately)
1. Select the "requirements.txt" file to install packages
1. Press OK

# Python localization

The GNU Translation tools are not installed on Windows by default. I install the
static 64-bit installer from here:

[gettext 0.21 and iconv 1.16 - Binaries for Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)

The installer creates a folder for the tools and puts them into your path.

- xgettext.exe &mdash; Parses source files for strings and copies them to a .PO file.

  `xgettext -p ./locale -d domain source.py [...]`


- msginit.exe &mdash; Starts a new translation from an existing one.

  `msginit -i en.po -o fr.po -l fr_FR`

- msgfmt.exe &mdash; Builds .PO files into .MO files, which are read by the program.

  `msgfmt -i en.po -o en.mo`

The .MO files must be stored in a folder structure like this:

  locale/_language_/LC_MESSAGES/_domain_.mo

> For this project, the text domain is `hello`.

# Useful Websites

* [W3School Python Tutorial](https://www.w3schools.com/python/default.asp) A
  quick refresher of Python syntax.

* [GNU `gettext` utilities](https://www.gnu.org/software/gettext/manual/gettext.html)
  The complete manual for GNU localization tools.

* [`gettext` - Multilingual internalization services](https://docs.python.org/3/library/gettext.html)
  Python's implementation of the GNU `gettext` API.

* [typing - Support for type hints](https://docs.python.org/3/library/typing.html)
  for Python syntax to support strongly typed arguments and return values.

* [pytest Documentation](https://docs.pytest.org/en/7.1.x/index.html) for examples
  of unit tests written for `pytest`.

* [Pytest With Eric](https://pytest-with-eric.com/pytest-best-practices/pytest-logging/)
