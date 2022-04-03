# Ibudget Server

## Requirements

- Python 3.7+
- MySQL 5.7+

## Installation

### Set up virtual environment

```shell
python3 -m venv venv
source ./venv/bin/activate
```

### Install dependencies

```shell
pip3 install -r requirements-dev.txt
```

### Install `pre-commit` hooks

- Install `pre-commit`: https://pre-commit.com/
- Install `pre-commit` hooks:

  ```shell
  pip3 install pre-commit
  pre-commit install
  ```

## Running

Inside the virtual environment, run

```shell
python3 run.py
```
