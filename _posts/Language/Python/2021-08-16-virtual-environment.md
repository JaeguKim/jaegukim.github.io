---
layout: post
title: "virtual environment"
date: 2021-08-16 22:49:00 +0900
categories: [Language,Python]
---

## venv 이용하는 방법

1. ```python3 -m venv [env name]```
2. ```source [env name]/bin/activate```

> venv 나가는 방법 : ```Ctrl + D```

## Poetry

### Why poetry
1. smarter dependency resolvement compared to pip
2. easier virtual env setting
3. easier packaging

### How to use
1. ```pip3 install poetry``` : install poetry
2. ```poetry shell``` : activate virtual env
3. Use following commands
    - ```poetry install``` : generate poetry.lock file and install dependencies
        - `--no-root` : install only dependencies
        - `--no-dev` : skip development dependencies
    - ```poetry update``` : update poetry.lock file