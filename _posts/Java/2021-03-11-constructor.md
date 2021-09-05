---
layout: post
title: "Constructor"
date: 2021-03-11 11:42:00 +0900
categories: [Language,Java]
---

## Super() 키워드가 자동으로 호출되는 경우

> Java에서는 자식 클래스가 생성될때, 상위 클래스의 모든 생성자가 먼저 호출된다. 자동으로 호출되는 경우는, 상위 클래스에서 parameterized constructor가 선언되어있지 않은경우 이다.

## Private Constructor 사용하는 경우

1. class내에 있는 **static factory method** 만을 사용해서 객체를 생성해야하는 경우
2. static 함수만 포함하고 있는 **utility class**의 경우