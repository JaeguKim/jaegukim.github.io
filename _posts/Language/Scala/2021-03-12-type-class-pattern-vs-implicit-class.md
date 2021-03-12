---
layout: post
title: "Type class pattern vs implicit class"
date: 2021-03-12 15:25:00 +0900
categories: [Language,Scala]
---

## Type class pattern vs implicit class

implicit class는 보통 존재하는 타입에 대한 extention method를 제공하는데 사용된다.

```scala
implicit class IntExt(val x: Int) extends AnyVal {
  def squared: Int = x * x
}

10.squared shouldEqual 1000
```

Type class는 ad-hoc polymorphism을 제공한다.

```scala
trait Show[T] {
  def show(x: T): String
}

implicit val intHexShow: Show[Int] = new Show[Int] {
  override def show(x: Int): String = Integer.toHexString(x)
}

implicit val stringReverseShow: Show[String] = new Show[String] {
  override def show(x: String): String = x.reverse
}

def showPrint[T](value: T)(implicit s: Show[T]): Unit = {
  println(s.show(value))
}

showPrint(12)  // prints "c"
showPrint("hello")  // prints "olleh"
```

파라미터의 타입에 맞는 Show 클래스를 생성하기때문에, ad-hoc polymorphism을 제공한다. 주로 존재하는 타입에 대해서 generic한 방식으로 새로운 behavior를 제공하고 싶을때 사용한다.

