---
layout: post
title: "Method Signature"
date: 2020-11-16 14:32:00 +0900
categories: [Java]
---

# Method Signature란?

Java에서 method signature란 함수명,파라미터의 타입,갯수,순서를 말한다. 리턴타입과 thrown exception들은 method signature의 일부로 간주되지 않는다.
예를 들면, 다음 두 메소드는 다른 signature를 가진다.

``` java
doSomething(String[] y);
doSomething(String y);
```

다음의 세 메소드들은 같은 signature를 가진다.

``` java 
int doSomething(int y) 
String doSomething(int x)
int doSomething(int z) throws java.lang.Exception
```