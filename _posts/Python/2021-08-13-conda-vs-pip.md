---
layout: post
title: "Conda vs Pip"
date: 2021-08-13 21:03:00 +0900
categories: [Python]
---

## Comparison of conda and pip

|                       | conda                   | pip                             |
| --------------------- | ----------------------- | ------------------------------- |
| manages               | binaries                | wheel or source                 |
| can require compilers | no                      | yes                             |
| package types         | any                     | Python-only                     |
| create environment    | yes, built-in           | no, requires virtualenv or venv |
| dependency checks     | yes                     | no                              |
| package sources       | Anaconda repo and cloud | PyPI                            |



## [Source](https://www.anaconda.com/blog/understanding-conda-and-pip)