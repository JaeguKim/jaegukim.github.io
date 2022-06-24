---
layout: post
title: "Trouble Shooting(Go)"
date: 2022-05-28 16:20:00 +0900
categories: [Language,Go]
---

## GoLand No Tests Were Run
test 함수내에 `fmt.printf` 를 사용하는경우, test가 실행되었다고 인식이 되지 않는다.
`fmt.println`을 사용해서 해결가능하다.
