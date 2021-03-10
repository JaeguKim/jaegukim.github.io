---
layout: post
title: "Scala return"
date: 2021-02-10 09:50:00 +0900
categories: [Language,Scala]
---

Scala에서는 return 키워드가 없다면 마지막 expression이 return value로 간주된다.

``` scala
def f() = {
  if (something)
    "A"
  else
    "B"
}
```

위의 코드의 경우 리턴타입은 ```String```이 된다.

``` scala
def f() = {
  if (something)
    "A"
  else
    "B"

  if (somethingElse)
    1
  else
    2
}
```

위의 코드의 경우 리턴타입은 ```Int```가 된다.