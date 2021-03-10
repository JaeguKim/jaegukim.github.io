---
layout: post
title: "Binary Numeric Promotion"
date: 2020-11-22 10:56:00 +0900
categories: [Java]
---

# Binary Numeric Promotion
operator가 binary numeric promotion을 operand들에게 적용할때, numeric type으로 변환되는 값을 명시해줘야 하며, 다음과 같은 규칙을 따른다.
순서대로 살펴보면 다음과 같다.

## 1. 만약 reference type이라면, unboxing conversion을 수행한다.

Unboxing Conversion이란 아래와 같은 변환을 말한다.

```
From type Boolean to type boolean

From type Byte to type byte

From type Short to type short

From type Character to type char

From type Integer to type int

From type Long to type long

From type Float to type float

From type Double to type double
```

## 2. Widening primitive conversion이 적용되는데, 규칙은 다음과 같다.

- 만약 operand중 하나가 double이면, 다른 것은 double로 변환한다.

- 그렇지 않으면, 만약 operand중 하나가 float이면, 다른것은 float로 변환한다.

- 그렇지 않으면, 만약 operand중 하나가 long이면, 다른것은 long으로 변환한다.

- 그렇지 않으면, 두 operand 모두 int로 변환한다.

## 3. 적용 Operators

Binary numeric promotion은 특정 operator들을 대상으로 수행된다.

- multiplicative operators * , / and %

- \+ and -

- < , <=, > and >=

- == and !=

- bitwise operators &, ^ and |

- conditional operators ? :

출처  
[https://docs.oracle.com/javase/specs/jls/se7/html/jls-5.html#jls-5.6.2](https://docs.oracle.com/javase/specs/jls/se7/html/jls-5.html#jls-5.6.2)