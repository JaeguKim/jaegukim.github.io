---
layout: post
title:  "Memory Management"
date:   2020-09-15
categories: [OS]
---
## **메모리관리의 목적**
다중 프로그래밍 실현을 위해 메모리에 많은 process들을 동시에 유지하기 위해서는 메모리 관리가 필요하다. 

## **Address Binding Time**
process들의 메모리 주소를 결정하는 시점(Address Binding Time)은 크게 3가지가 있다.
- compile time binding : 만일 process가 memory내에 들어갈 위치를 컴파일 시간에 미리 알수있는 경우

- load time binding : 이진코드를 재배치 가능 코드로 만들수 있는 경우

- execution time binding : process가 실행하는 중간에 memory 내의 한 segment에서 다른 segment로 옮겨질수 있는 경우

## **Virtual Memory**
- 프로세스 전체가 메모리 내에 올라오지 않더라도 실행이 가능하도록 하는 기법

## **Logical vs Physical Address**

* logical address : cpu가 생성하는 주소

* physical address: 메모리가 취급하는 주소

- compile-time binding과 load-time binding에서는 logical address와 physical address가 같다.

- execution-time binding에서는 다르다.

## **Paging**
- OS가 보조기억장치에 있는 프로그램을 동일한 크기의 블록으로 나누어서 관리하는 기법

## **DemandPaging**
- 실행프로그램이 요구할때 비로소 보조기억장치에서 주기억장치로 적재하는 방법

## **MMU(Memory Management Unit)**
virtual(logical) addr를 physical addr로 변환하는 역할을 한다.

## **Dynamic Loading** 
각 routine이 재배치 가능 상태로 디스크에 대기하다가, 필요할때 적재. 사용되지 않는 routine은 적재 되지 않는다.

## **Dynamic Linking** 
linking이 실행시간 까지 미루어짐. 라이브러리를 부르는 곳마다 stub이 생겨서 메모리를 찾는방법과 없을경우 라이브러리 적재방법을 알려준다.

## **Swapping** 
일시적으로 process를 main memory에서 disk로 이동시켰다가 다시 memory로 이동시키는것.
* 목적 : process들을 실행하는데 필요한 공간이 physical memory공간을 초과할때 사용
* roll in, roll out : 더 높은 우선순위의 process가 swap-in 되고 더 낮은 우선순위의 procss가 swap-out 되는것

## **Contiguous Memory Allocation 기법: 연속적으로 memory 할당**
- First Fit : 충분히 큰 첫번째 구멍에 할당

- Best Fit : 충분히 큰 가장 작은 구멍에 할당

- Worst Fit : 가장 큰 구멍에 할당
일반적으로 first fit, best fit이 worst fit보다 성능이 좋다.

## **Fragmentation**
- External Fragmentation : 충분한 전체 memory 공간이 있지만, 연속적이지 않음

    줄이는 법 : Compaction(메모리의 모든 내용들을 한군데로 몰고 모든 자유공간을 한군데로 몰아서 큰블록을 만드는 것)기법, 하지만 비용이 많이 들고 프로세스들의 재배치가 실행시간에 동적으로 이루어지는 경우만 가능

- Internal Fragmentation : 할당된 공간이 요구된 공간보다 약간 큰 경우, 두 크기의 차이로 인하여 internal fragmentation이 발생한다.
