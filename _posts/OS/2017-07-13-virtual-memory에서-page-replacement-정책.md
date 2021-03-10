---
layout: post
title: "Virtual memory에서 page replacement 정책"
date: 2017-07-13
categories: [OS]
---
# FIFO

- memory에 올라온 시간이 가장 오래된 page를 victim으로 선정

- optimal 하지는 않지만 correctnesss에 영향을 주지는 않음

- 단점 : Belady's anomaly 발생

## Belady's anomaly란?

- frame 수는 증가했지만, page fault는 오히려 증가하는 현상

# Optimal Page Replacement

- 가장 오랜기간동안 사용되지 않을 page를 선택

- 할당된 frame수가 고정일때 가장 낮은 page 부재율을 보장

- 구현이 어려움(앞으로 process가 메모리를 어떻게 참조할지 알아야 하므로)

# LRU page Replacement

- optimal algorithm에 대한 근사

- 과거를 가까운 미래의 근사치로 본다

- 가장 오랫동안 사용되지 않은 page를 선택, 

- Belady의 모순현상 없음

- 단점 : 프로세스가 main memory에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야함(오버헤드 발생)
