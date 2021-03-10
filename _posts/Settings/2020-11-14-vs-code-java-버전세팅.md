---
layout: post
title: "VS Code에서 java 버전 수동으로 세팅하기"
date: 2020-11-14 09:12:00 +0900
categories: [Settings]
---

Java Intellisense를 VS code에서 사용하려면 Java11 이상 버전이 필요하다고 한다. 하지만 외부 터미널에서는 계속 Java8을 사용하고 싶다면, 다음과 같이 하면된다.
1. Preferences -> Settings
2. 검색창에 Java라고 검색
3. Java:Home 섹션 밑에 Edit in settings.json 선택
4. 다음 라인추가
``` json
    "java.home": "/Library/Java/JavaVirtualMachines/jdk-14.0.2.jdk/Contents/Home"
```
