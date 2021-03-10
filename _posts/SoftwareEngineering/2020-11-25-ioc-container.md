---
layout: post
title: "[Inversion of Control 이해하기] Chapter 4 - IoC Container"
date: 2020-11-25 22:11:00 +0900
categories: [SoftwareEngineering]
---

# IoC Container

IoC Container(DI Container)는 automatic dependency injection을 구현하기 위한 프레임워크이다. IoC는 객체생성과 life-time을 관리하고 클래스에 대한 의존성을 주입한다.

IoC 컨테이너는 **run time**에 특정 class 객체를 생성하고 모든 dependency 객체들을 constructor, property 또는 method를 통해서 주입하며, 적절한 시기에 이들을 소멸시킨다. 이 모든과정이 우리가 신경쓸 필요없이 자동으로 일어난다. 따라서 수동으로 객체들을 생성하고 관리할 필요가 없어진다.

모든 컨테이너들은 다음의 DI lifecycle을 손쉽게 지원할수 있어야한다.

## Register
컨테이너는 특정 타입에 대하여 어떤 dependency를 instantiate할것인지 알 수 있어야한다.
기본적으로 type-mapping을 등록하는 방법을 포함해야한다.

## Resolve
IoC 컨테이너를 사용할때, 수동으로 객체를 생성할 필요가 없어야한다. 컨테이너가 대신 해주기 때문이다. 이것을 resolution이라고 부른다. 컨테이너는 특정 타입을 resolve 하기 위해서 몇몇 함수들을 포함해야한다. 컨테이너는 특정 타입에 대한 객체를 생성하고 의존성이 존재한다면 의존성을 주입하고, 객체를 리턴한다.

## Dispose
컨테이너는 dependent 객체들의 lifetime을 관리해야만한다. IoC 컨테이너들은 객체들의 lifecycle을 관리하고 소멸하는 고유한 life time manager들을 가지고 있다.

## 후기
지금까지 IoC를 이해하기 위한 포스팅을 마친다. 나중에는 Spring의 IoC 컨테이너에 대해서 공부해볼 예정이다.

## 출처
[https://www.tutorialsteacher.com/ioc/ioc-container](https://www.tutorialsteacher.com/ioc/ioc-container)