---
layout: post
title: "fold,foldLeft,foldRight"
date: 2021-04-05 17:20:00 +0900
categories: [Language,Scala]
---

## 예시
``` scala
    val numbers = List(5, 4, 8, 6, 2)
    val res = numbers.fold(0) { (z, i) =>
      z + i
    }
    // result = 25
```

## 동작방식
At the start of execution, the start value that you passed as the first argument is given to your function as its first argument. As the function's second argument it is given the first item on the list (in the case of fold this may or may not be the actual first item on your list as you will read about below).

1. The function is then applied to its two arguments, in this case a simple addition, and returns the result.

2. Fold then gives the function the previous return value as its first argument and the next item in the list as its second argument, and applies it, returning the result.

3. This process repeats for each item of the list and returns the return value of the function once all items in the list have been iterated over.

4. This is a trivial example though. Let's take a look at something that is more useful. I will use foldLeft in this next example and will explain how it is different from fold later. For now, think of it in the same way as fold.


## fold,foldLeft,foldRight 차이점
fold operation이 순회하는 순서의 차이가 있다.
foldLeft는 맨 왼쪽에서 시작하여 오른쪽으로 순회해나간다, foldRight은 맨 오른쪽에서 시작하여 왼쪽으로 순회해나간다. fold의 경우는 특정 방향이 정해져있지 않다.

fold가 방향이 정해져있지 않으므로 두가지 제약조건이 존재한다. : start value, return value
첫번째 제약조건 : start value는 folding하는 object의 super type이어야한다.
첫번째 예시에서 보면, List[Int] 타입에 대해서 folding하고 있고 start value type은 Int이다. Int는 List[Int]의 supertype이다.
두번째 제약조건 : start value must be neutral, 즉 결과를 바꿔서는 않된다. 예를 들면, 덧셈연산에서 neutral value는 0이고 곱셈연산에서는 1이다. 

## 출처
[https://coderwall.com/p/4l73-a/scala-fold-foldleft-and-foldright](https://coderwall.com/p/4l73-a/scala-fold-foldleft-and-foldright)