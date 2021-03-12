---
layout: post
title: "Case Class"
date: 2021-03-12 15:39:00 +0900
categories: [Language,Scala]
---

## Case Class

> regular class와 몇가지 특성을 제외하고 비스한다. immutable data를 모델링하는데 좋다.

### case class 정의하기

``` scala
case class Book(isbn: String)

val frankenstein = Book("978-0486282114")
```

```Book``` case class를 생성할때 new 키워드가 사용이 되지 않음을 알수 있다. 이유는 case class가 apply method를 기본적으로 가지고 있어서, object 생성을 하기 때문이다.

``` scala
case class Message(sender: String, recipient: String, body: String)
val message1 = Message("guillaume@quebec.ca", "jorge@catalonia.es", "Ça va ?")

println(message1.sender)  // prints guillaume@quebec.ca
message1.sender = "travis@washington.us"  // this line does not compile
```

val로 message1이 선언되었기 때문에, ```message1.sender```  에 값을 재할당해줄수는 없다. var로 선언할순 있지만 추천하지 않는다.

## 비교

case class들은 reference가 아닌 structure로 비교된다.

```scala
case class Message(sender: String, recipient: String, body: String)

val message2 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
val message3 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
val messagesAreTheSame = message2 == message3  // true
```

## 복사

``` copy ``` 함수를 이용해서 case class의 객체를 (shallow)copy 할수 있다.

``` scala
case class Message(sender: String, recipient: String, body: String)
val message4 = Message("julien@bretagne.fr", "travis@washington.us", "Me zo o komz gant ma amezeg")
val message5 = message4.copy(sender = message4.recipient, recipient = "claire@bourgogne.fr")
message5.sender  // travis@washington.us
message5.recipient // claire@bourgogne.fr
message5.body  // "Me zo o komz gant ma amezeg"
```

여기서는 body는 직접 복사되고 나머지 필드는 새로 값이 할당된다.

## 출처

[https://docs.scala-lang.org/tour/case-classes.html](https://docs.scala-lang.org/tour/case-classes.html)

