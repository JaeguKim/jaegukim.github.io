---
layout: post
title: "static"
date: 2021-04-15 11:28:00 +0900
categories: [Java]
---

## Static Method

static이라는 의미는 data가 어느 특정 객체에 속할필요가 없다는것을 의미한다. static method나 class를 생성하면 heap의 특별한 공간에 저장된다 : PermGen(Permanent Generation), 이 공간은 클래스에 적용되는 모든 non-instance 데이터를 가지고 있는 공간이다. Java8 부터는 PermGen이 아니라 Metaspace에 저장되게 되었다. Metaspace와 PermGen의 차이는, PermGen은 고정된 크기의 메모리 공간을 소유하고, Metaspace는 auto-growing 메모리 공간을 소유한다는 것이다. 그리고 이 Metaspace는 모든 인스턴스들에의해서 공유된다. Metaspace는 또한 Native Memory의 일부이다.

> static 변수는 객체가 생성되는 시점이 아닌, JVM에 클래스가 로드되는 시점에 초기화 된다. 

## Static class in Java

Java allows a class to be defined within another class. These are called **Nested Classes**. The class in which the nested class is defined is known as **Outer Class**. 

- Inner class : Non static nested class class.

- Static class : static nested class

## Static nested class 특징

1. can be instantiated without outer class
2. Unlike Inner class can access both static and non-static members of the outer class, static class can only access static members of the outer class.

## 출처
[https://www.linkedin.com/pulse/static-variables-methods-java-where-jvm-stores-them-kotlin-malisciuc/](https://www.linkedin.com/pulse/static-variables-methods-java-where-jvm-stores-them-kotlin-malisciuc/)
