---
layout: post
title: "Dockerfile에서Container 환경변수 수정하기"
date: 2021-08-30 15:02:00 +0900
categories: [Docker]
---

먼저 ```alias python=python3``` 를 추가하고 싶다고 하자.

## Interactive Shell에만 적용하고 싶은 경우

``` Dockerfile
RUN echo 'alias python=python3' >> ~/.bashrc
RUN echo 'PYSPARK_PYTHON=python3' >> ~/.bashrc
```

## Non Interactive shell에도 적용하고 싶은 경우

``` Dockerfile
RUN echo -e '#!/bin/bash\nalias python=python3' > /usr/bin/update_alias && \
    chmod +x /usr/bin/update_alias && update_alias
```