# py-csc

Programming fundamentals in Python.

## Prerequisites

Install the following.

- Python 3.9
- [pyenv](https://github.com/yyuu/pyenv)
- [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

Create a virtual environment for this project.

```bash
$ pyenv virtualenv 3.9.1 csc
```

## Install

```bash
$ git clone https://github.com/dtjv/py-csc.git
$ cd py-csc
$ pyenv local csc
(csc) $ make
(csc) $ make precommit
```

## Run Tests

```bash
$ make test
```

## Author

- [David Valles](https://dtjv.io)

## License

[MIT License](LICENSE).
