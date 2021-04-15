---
layout: post
title: "static class"
date: 2021-04-15 11:28:00 +0900
categories: [Java]
---

## Static class in Java

Java allows a class to be defined within another class. These are called **Nested Classes**. The class in which the nested class is defined is known as **Outer Class**. 

- Inner class : Non static nested class class.

- Static class : static nested class

## Static nested class 특징

1. can be instantiated without outer class
2. Unlike Inner class can access both static and non-static members of the outer class , static class can only access static members of the outer class.