---
layout: post
title: "Trouble shooting log(Python)"
date: 2021-10-09 17:54:00 +0900
categories: [Language,Python]
---

## OSError: mysql_config not found when installing ```mysqlclinet```
- solution : install mysql on your mac by ```brew install mysql```

## `pip install cryptography` 설치시 에러 발생
운영체제별로 다음 [실행과정](https://cryptography.io/en/3.4.8/installation.html) 수행

## [error 32] broken pipe 에러
kafka producer app에서 prometheus로 쿼리를 할때 prometheus에서 설정해둔 request timeout값을 넘긴 경우, prometheus에서 connection을 close하게 되고 결과적으로 클라이언트에서 broken pipe에러를 보게되는것으로 추정된다.

