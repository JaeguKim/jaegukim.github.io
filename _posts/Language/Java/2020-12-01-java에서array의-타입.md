---
layout: post
title: "Java에서 array의 타입"
date: 2020-12-01 13:37:00 +0900
categories: [Language,Java]
---

자바에서 배열은 primitive type인가 아니면 object인가?
위와 관련해서 [다음 글](https://www.tutorialspoint.com/is-an-array-a-primitive-type-or-an-object-in-java)을 찾아보았고 번역해보았다.

Java에서 Array는 **object**로 간주된다. 이유는 array가 **new** 키워드로 생성될수 있기 때문이다. **new** 키워드는 항상 **object**를 생성하기 위해서 사용된다.
array의 direct parent class or super class는 **'Object'** class이고 Java에서 모든 array type은 특정 클래스에 속한다. 이점은 integer array type에, double array types, float array types ... 에 대해서 명시적인 클래스가 존재함을 뜻한다.

## 예시
 
 ``` java
 public class Demo{
   public static void main(String[] args){
      System.out.println("Is the argument an instance of super class Object? ");
      System.out.println(args instanceof Object);
      int[] my_arr = new int[4];
      System.out.println("Is the array my_arr an instance of super class Object? ");
      System.out.println(my_arr instanceof Object);
   }
}
```

## 출력

```
Is the argument an instance of super class Object?
true
Is the array my_arr an instance of super class Object?
true
```

위의 결과를 볼때 int[] my_arr는 Object class 타입인 것을 알수있다.