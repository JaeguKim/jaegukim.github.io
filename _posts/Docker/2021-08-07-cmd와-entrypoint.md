---
layout: post
title: "RUN CMD vs ENTRYPOINT"
date: 2021-08-07 23:12:00 +0900
categories: [Docker]
---

## 요약

- `RUN` executes command in a new layer and creates a new image.
- `ENTRYPOINT` : ENTRYPOINT를 사용해서 컨테이너 수행 명령을 정의하면, 지정한 명령대로 무조건 실행이 된다.
- `CMD` : 컨테이너 실행시 지정한 인자값을 실행하도록 할수 있음.

## 실험

``` dockerfile
FROM ubuntu
CMD ["bin/df", "-h"]
```

먼저 ``` docker build -t jgkim/df . ``` 로 빌드하자.

 ```docker run --name jgkim-df jgkim/df ``` 이렇게 하게되면 파일 내에 지정된 커멘드가 실행이 된다.

반면 ```docker run --name jgkim-df jgkim/df ps -aef``` 이런 식으로 하게 되면 CMD에 지정된 내용대신 ```ps -aef``` 가 실행이된다.

``` dockerfile
FROM ubuntu
ENTRYPOINT ["bin/df", "-h"]
```

반면 위처럼 실행하면 항상 지정된 커멘드만 실행이 된다.

## [출처](https://bluese05.tistory.com/77)


