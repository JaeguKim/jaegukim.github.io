---
layout: post
title: "Kafka Trouble Shooting"
date: 2020-12-04 23:35:00 +0900
categories: [DataEngineering,Kafka]
---

## The process cannot access the file because it is being used by another process.

위 경우는 다른 카프카가 이미 해당 파일을 사용하고 있기 때문에 발생한다. 가장 빠른 방법은 카프카 포트번호(default 9092)를 사용중인 카프카를 종료시키고 재실행하는 것이다.
즉, 9092 포트를 사용중인 프로세스를 종료시키면된다. 

```
sudo lsof -t -i tcp:9092 | xargs kill -9
```

mac 기준이라 다른환경에서는 잘모르겠다.
