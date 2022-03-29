---
layout: post
title: "Testing Github Action in local"
date: 2022-03-29 14:34:00 +0900
categories: [DevOps]
---

## Using custom docker image for local test

1. Install [act](https://github.com/nektos/act)
    - ```brew install act```
2. Build custom docker image

``` sh
    docker build -t local-airflow-ci .  -f ./Dockerfile.ci --build-arg AIRFLOW_VERSION=2.1.4-buster
```
3. Test specific job

``` sh
act -W ./.github/workflows/pull_request_ci.yml -P self-hosted=local-airflow-ci  -j pylint
```
