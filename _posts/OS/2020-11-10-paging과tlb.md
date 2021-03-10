---
layout: post
title: "Paging과 TLB"
date: 2017-07-13
categories: [OS]
---

# Paging
가상기억장치를 모두 같은 크기의 페이지 블록으로 편성하여, 각각의 페이지 블록들이 실제 물리 프레임에 맵핑 되도록 구성하는 기법, 논리주소 공간이 한 연속적인 공간에 모여 있어야 하는 제약조건을 없앤다.

# Paging을 할때 어떻게 실제 메모리 주소에 데이터를 전송하는가?
페이지 번호와 페이지 변위로 구성된 가상주소를 가지고 page table에 접근하여, page 번호와 일치되는 행의 프레임 번호를 찾고 그 위치와 page offset을 더하여 실제 메모리 주소에 접근한다.

# Page table에 저장되는 항목
page 번호,해당 페이지에 할당된 물리 메모리(프레임)의 시작 주소

# Page table이 저장되는 장소 
메인메모리

# Page table접근 속도 향상시키는 방법
## TLB(Transition Look-aside Buffer) 이용
- TLB는 page table entry에 대한 특수한 소형 하드웨어 캐시이다. 

- TLB는 Page table의 일부를 저장한다

- 만약 페이지 번호가 연관 register TLB에서 찾아지지 않으면 main memory에 있는 page table에서 찾으면 된다.
