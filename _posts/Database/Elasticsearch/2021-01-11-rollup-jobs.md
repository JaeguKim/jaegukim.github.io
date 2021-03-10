---
layout: post
title: "Rollup Jobs"
date: 2021-01-11 22:23:00 +0900
categories: [Database,Elasticsearch]
---

## Rollup Jobs
rollup job이란 인덱스 패턴에의해 명시된 인덱스들의 데이터를 집계하여 새로운 인덱스에 저장하는 주기적인 task를 말한다. Rollup 인덱스들은 시각화와 리포트 생성을 위해서 수개월, 수년의 historical data들을 compact하게 저장하기위한 좋은 방법이다.
현재는 X-Pack에있는 기능이다.