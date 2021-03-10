---
layout: post
title: "캐시가 필요한 이유와 Cache Hit Ratio"
date: 2017-07-12
categories: [Architecture]
---

# 캐시가 필요한 이유
대부분 프로그램은 한번 사용한 데이터를 다시 사용할 가능성이 높고, 그 주변의 데이터도 곧 사용할 가능성이 높은 데이터 지역성을 가지고 있다.  
데이터 지역성을 활용하여 메인 메모리에 있는 데이터를 캐시 메모리에 불러와 두고, CPU가 필요한 데이터를 캐시에서 먼저 찾도록 하면 시스템 성능을 향상시킬 수 있다.

- cache hit : 참조하려는 데이터가 캐시에 존재할때 캐시 히트

- cache miss : 참조하려는 데이터가 캐시에 존재하지 않을때 캐시 미스

# Cache hit ratio
> cache hit ratio = (캐시히트횟수)/(전체 참조횟수)  
평균접근시간 = cache hit ratio * 캐시접근시간 + (1-cache hit ratio) *메인 메모리 접근시간  
단, 캐시 접근시간 << 메인 메모리 접근 시간