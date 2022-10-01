# Python Password Manager

This is repo contains code that I generate while working on the [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) udemy course for learning Python.

This repo covers the project for days 29 and 30 of the course.

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/darkstar-holdings-edu/python_password_manager)
![GitHub](https://img.shields.io/github/license/darkstar-holdings-edu/python_password_manager)

## WARNING

This is just a learning project. Don't actually use this if you care about security. The passwords are stored in a `data.json` file in clear text. There should be no expectation of security! You've been warned.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The things you need before installing the software.

- [pipenv](https://pipenv.pypa.io/en/latest/index.html) [^1]

[^1]: Note: I use `pipenv` because I like the combination of the `venv` and `pip` commands together. However, I know it's not for everyone. So I've created a `requirements.txt` file if you don't like `pipenv` and just want to use `pip` instead.

### Installation

```sh
pipenv install --dev
pipenv shell
```

## Usage

- `main.py`: Executable to launch the application.

## License

Distributed under the MIT License. See [LICENSE](https://github.com/darkstar-holdings-edu/python_password_manager/blob/master/LICENSE) for more information.
