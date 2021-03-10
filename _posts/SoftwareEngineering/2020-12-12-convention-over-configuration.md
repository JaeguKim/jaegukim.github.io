---
layout: post
title: "Convention over configuration"
date: 2020-12-12 23:07:00 +0900
categories: [SoftwareEngineering]
---

## Convention over configuration

프레임워크를 사용하는 개발자가 결정해야하는 것들을 flexibility감소 없이 감소시키는것.

예를들면, Sales라는 클래스가 model에 존재하고, 그 클래스에 대응하는 table은 기본적으로 "Sales"라고 불리는데, 오직 이러한 convention에 벗어날때만 (product sales같은) 개발자가 이름을 변경하는 코드를 작성하게 하는것.