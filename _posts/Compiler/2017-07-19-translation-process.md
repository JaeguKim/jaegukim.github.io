---
layout: post
title: "Translation Process"
date: 2017-07-19
categories: [Compiler]
---
![img](/assets/img/post/Compiler/2017-07-19-translation-process.png)

- Scanner의 역할은 character stream을 가지고 token(의미를 가지는 최소단위)을 생성하는것이다.

- Parser의 역할은 일련의 token들을 가지고 syntax tree/parse tree를 생성하는 것이다.

- Semantic analyzer는 parse tree를 가지고 프로그램의 의미를 분석하는 일을 한다.

- Source code optimizer는 syntax tree를 좀더 간략하게 만들고 three-address code를 좀더 심플하게 만드는 역할을 한다.

- Code generator는 target machine으로 변환시키는 역할을 한다.

- Target code optimizer는 target code를 개선시키는 역할을 한다.