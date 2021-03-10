---
layout: post
title: "Design Principle vs Design Pattern"
date: 2020-11-25 18:40:00 +0900
categories: [SoftwareEngineering]
---

Software engineering에서 design principle과 design pattern은 같지 않다.

# Design Principle

- Design Principle은 소프트웨어를 잘 디자인하기 위한 high level 가이드라인을 제공한다.

- 구현에 대한 가이드라인은 제공하지 않는다. 

- 대표적으로는 SOLID(SRP, OCP, LSP, ISP, DIP)가 있다.

- 예를들어, Single Responsibility Principle (SRP)는 모든 클래스는 하나의 책임만 가지며, 클래스는 그 책임을 완전히 캡슐화해야 함을 일컫는다.

# Design Pattern

- object-oriented problem에 대하여, 구현과 관련하여 low level 솔루션들을 제공한다.

- 특정한 object-oriented problem에 대하여 구현방법을 제공한다.

- 만약, 한번에 하나의 오브젝트만 가져야하는 클래스를 만든다면 Singleton design pattern을 사용할수 있다.

- Design Pattern은 많은 사람들에 의해서 테스트되었고, 검증되어있다.

## 출처
[https://www.tutorialsteacher.com/articles/difference-between-design-principle-and-design-pattern](https://www.tutorialsteacher.com/articles/difference-between-design-principle-and-design-pattern)