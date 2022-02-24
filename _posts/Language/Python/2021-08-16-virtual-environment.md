---
layout: post
title: "virtual environment"
date: 2021-08-16 22:49:00 +0900
categories: [Language,Python]
---

## venv 이용하는 방법

1. ```python3 -m venv [env name]```
2. ```source [env name]/bin/activate```

> How to escape : ```Ctrl + D```

## pyenv

> you can use multiple python by using `pyenv`

### How to install (in Mac)
```sh 
    brew update
    brew install pyenv
    echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### How to use
1. Install additional python : ```pyenv install [python version]``` eg. `pyenv install 3.9.7`
2. Setup python in current directory : `pyenv local [python version]` eg. `pyenv local 3.9.7` 
3. Unset python in current directory : `pyenv local --unset`

## Poetry

### Why poetry
1. smarter dependency resolvement compared to pip
2. easier virtual env setting
3. easier packaging

### How to use
1. ```pip3 install poetry``` : install poetry
2. ```poetry shell``` : activate virtual env
    - `deactivate` : stop virtual env
3. Use following commands
    - ```poetry install``` : generate poetry.lock file and install dependencies
        - `--no-root` : do not install root packages(your project)
        - `--no-dev` : skip development dependencies
    - ```poetry update``` : update poetry.lock file
    - ```poetry run [command]``` : run command in virtual env
    - ```poetry add ``` : adds required packages to your `pyproject.toml`
        - eg. ```poetry add pendulum@^2.0.5``` or ```poetry add "pendulum>-2.0.5```

- Using different python version
    - ```poetry env use python3.x``` or ```poetry env use 3.x```
