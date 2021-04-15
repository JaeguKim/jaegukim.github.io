---
layout: post
title: "Java Servlet"
date: 2021-04-15 15:22:00 +0900
categories: [Spring]
---

## Java Servlets

> Java Web Application에 URL mapping, request handling 기능을 제공하는 class

Java server는 JVM위에서 동작하고, Java Application은 Java Server위에서 동작한다. 그리고 Java server의 기능을 사용하기 위해서 Java Servlet API를 사용한다.

<img src="https://images.idgesg.net/images/article/2018/10/jw-servlet-fig2-100776897-medium.jpg" alt="jw servlet fig2"  />

Java Servlet 명세에는 Java Server와 관련 component에 대한 정의를 포함하고 있다. 오늘날 대부분의 Java server는 Servlet 4.0과 호환된다. Java server를 다른말로 Servlet container라고도 부른다. Servlet을 생성하기 위해서는 ```Servlet``` 인터페이스를 구현하여 servlet container(Java Server) 내에서 배포해야한다. 대표적인 Servlet container로 Tomcat, Jetty가 있다. 