---
layout: post
title: "Garbage Collection"
date: 2021-03-04 22:08:00 +0900
categories: [Language,Java]
---

## Garbage Collection 동작방식

Java garbage collection은 라이브 오브젝트들을 추적하고 다른 오브젝트들은 garbage로 간주한다.

OS는 미리 JVM이 필요한 heap영역을 할당한다. 

- 객체생성이 더 빠르다(OS가 관여하지 않기 때문). 메모리할당은 메모리 배열의 일부를 차지하고 offset을 앞으로 옮기기만 하면된다. 다음 할당은 이 offset부터 시작한다.
- 객체가 더이상 사용되지 않으면, garbage collector가 메모리를 다시 차지하고 추후 객체할당에 사용한다. 이는 아무런 명시적인 삭제가 없음을 의미하고, 메모리가 OS에 반환되지 않음을 의미한다.

![img](https://dt-cdn.net/images/allocation-350-c9ff036516.webp)

모든 객체들은 JVM이 관리하는 heap에 할당된다. 개발자가 사용하는 모든 아이템은 이러한 방식으로 처리된다. 객체가 reference될때 JVM은 alive라 판단한다. 객체가 코드에서 참조되지 않으면, garbage collector는 해당 메모리를 되찾는다.

## Garbage Collection Root

모든 오브젝트 트리는 한개 이상의 루트 오브젝트를 가진다. 앱이 그 루트에 접근가능하다면, 모든 트리는 reachable이다. 그렇다면 언제 reachable한것인가? garbage-collection root라 불리는 특별한 객체들은 항상 reachable이고 그것의 자식 객체들또한 reachable하다.

GC root에는 4가지가 존재한다.

- Local variable : 실제 객체가 아닌 virtual reference이다. 
- Active Java thread
- Static variable : 클래스들에 의해서 참조된다. 클래스 자체는 garbage-collected 가능하고 참조되는 static 변수들또한 garbage-collected될수 있다.
- JNI Reference : JNI call의 일부로 네이티브 코드가 생성한 자바 객체이다. JVM은 이 객체들이 네이티브 코드에 의해서 참조되는지 모르기 때문에, 이 객체는 생성되어야한다. 

![img](https://dt-cdn.net/images/gc-roots-459-1d9223317f.webp)

## Garbage 표시하고 정리하기

객체가 사용되지 않는지 판단하기 위해서, JVM은 **mark-and-sweep algorithm** 을 수행한다. 

1. 알고리즘은 GC root에서 시작하여, 모든 객체 reference를 순회하고 alive 객체들을 표시한다.
2. 표시된 객체들이 차지하고 있는 heap 메모리를 제외한 나머지 공간은 반환된다.

앱에 의해서 여전히 reachable하지만 사용되지 않는 객체들도 있을수 있다. 그러한 객체들은 garbage collect될수 없다. 그러한 logical memory leak은 어느 소프트웨어로도 감지할수 없다. 

![img](https://dt-cdn.net/images/gc-roots-with-memory-leak-434-3445cffac9.webp)

## [자세한 추가설명](https://d2.naver.com/helloworld/1329)

