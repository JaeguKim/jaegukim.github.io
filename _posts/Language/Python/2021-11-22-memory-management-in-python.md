---
layout: post
title: "Memory Management in Python"
date: 2021-11-22 23:54:00 +0900
categories: [Language,Python]
---

## Memory Management in Python

Python에서 메모리 관리는 python interpreter에 의해서 수행된다. 

### Default Python Implementation

default python implementation은 CPython으로, C로 구현이 되어있으며 다음 역할을 수행한다.

- code를 byte code로 변환
- byte code를 machine에서 실행

CPython에서 모든 타입들은 `PyObject` 구조체의 하위 타입이다. 구조체는 다음의 두가지 변수를 포함한다.

- ob_refcnt 
  - reference count
  - garbage collection에 사용됨

- ob_type 
  - python object 타입을 저장

각각의 객체는 object-specific memory allocator와 deallocator를 가지며, 다음 역할을 수행한다.

- allocator는 객체를 저장할 공간을 획득한다.

- deallocator는 객체가 사용되지 않으면, 메모리를 해제한다.

이때 여러 프로세스가 같은 시점에 메모리에 접근하면 문제가 발생할 수 있다. 

### Global Interpreter Lock(GIL)

GIL은 메모리와 같은 공유자원을 다루는데 있어서 해결책을 제공한다. 한 스레드가 공유된 자원에 사용하려고 할때 GIL을 획득하여, 다른 스레드가 동시에 사용할 수 없도록 한다. GIL은 전체 interpreter에 lock을 건다.

### Garbage Collection

reference count가 증가하는 경우는 아래와 같다.

1. 다른 변수에 할당할때

``` python
numbers = [1, 2, 3]
# Reference count = 1
more_numbers = numbers
# Reference count = 2
```

2. 객체를 인자로 전달할때

``` python
total = sum(numbers)
```

3. 객체를 리스트에 포함할때

``` python
matrix = [numbers, numbers, numbers]
```

reference count가 0이 되면, 객체에 정의된 특정 deallocation function이 실행되어 메모리를 해제한다.

### CPython's Memory Management

![img](https://files.realpython.com/media/memory_management.92ad564ec680.png)

Python의 메모리는 object storage(int,dict,...)와 non-object storage로 구분된다.

memory allocator의 디자인은 한번에 적은 양의 데이터를 할당하도록 되어있고(대부분의 python object는 크기가 작으므로), 반드시 필요한 시점에 메모리를 할당한다. 

#### Python memory allocation strategy

Python은 메모리 공간을 Arena라는 단위로 구성하고, 메모리의 page 바운더리로 정렬한다. Python은 page 사이즈를 256KB로 가정한다.

![Book with Page filled with Arena, Pools, and Block](https://files.realpython.com/media/memory_management_5.394b85976f34.png)

Arena 안에는 Pool들이 존재하는데, 4KB 크기의 virtual memory page를 갖고 있다. 이 Pool은 Block들로 나누어진다.

Block들은 같은 `size class` 들로 나타내진다. `size class` 는 요청된 데이터의 양에 따라서 특정 block size를 정의한다. 아래의 차트는 소스코드 코멘트에 있는 차트이다.

| Request in bytes | Size of allocated block | Size class idx |
| ---------------- | ----------------------- | -------------- |
| 1-8              | 8                       | 0              |
| 9-16             | 16                      | 1              |
| 17-24            | 24                      | 2              |
| 25-32            | 32                      | 3              |
| 33-40            | 40                      | 4              |
| 41-48            | 48                      | 5              |
| 49-56            | 56                      | 6              |
| 57-64            | 64                      | 7              |
| 65-72            | 72                      | 8              |
| …                | …                       | …              |
| 497-504          | 504                     | 62             |
| 505-512          | 512                     | 63             |

예를들어, 42 byte가 요청되면 데이터는 48 byte크기의 블럭에 위치하게 된다.

##### 1. Pools

`pool` 은 세가지 상태를 갖는다. 

1.  `used` : 데이터가 저장될 블럭들을 가짐.
2.  `full` : 공간이 모두 할당된 블럭들을 가짐.
3.  `empty` : 데이터가 없고, 어떤 size class도 할당가능하다.

각각의 pool은 다른 풀들에 대해서 double-linked-list를 유지한다. 이런방식으로 다른 풀들의 block에 존재하는 available space를 쉽게 찾을 수 있다.

`usedpools list` : available space를 갖는 pool들을 트래킹한다. block size 요청이 들어오면, 알고리즘은 `usedpools list` 에서 block size를 갖는 pool들을 체크한다.

`freepools list` : empty state에 있는 모든 pool들을 기록한다. 코드에서 8byte 크기의 메모리를 요청한다고 가정하자, 만약 `usedpools list` 에 아무런 pool이 없다면, empty pool이 8byte 블럭들을 저장할 수 있도록 초기화 된다. 그리고 이 새로운 pool은 `usedpools list` 에 추가되고 미래의 요청에 사용된다.

`full pool` 이 block들을 해제하면, 해당 pool은 `usedpools list` 로 다시 추가된다.

##### 2. Blocks

![Diagram of Used, Full, and Emtpy Pools](https://files.realpython.com/media/memory_management_3.52bffbf302d3.png)

block은 3가지 상태중 하나를 갖는다.

- untouched : 할당 된적 없는 메모리
- free : 할당은 되었었지만 나중에 해제된 메모리
- allocated : 현재 데이터를 저장하고 있는 메모리

### 3. Arenas

Arenas는 pool들을 포함한다. 이 pool 들은 `used`, `full`, `empty` 상태 중 하나이다. Arena 자체는 어떤 상태를 갖고 있진 않다. Arena들은 doubly linked list로 연결되어있다. 리스트는 free pool의 수로 정렬이 되어있다. free pool 수가 작을 수록 리스트의 앞 부분에 위치하게 된다.

![usable_areas Doubly-linked List of Arenas](https://files.realpython.com/media/memory_management_6.60e9761bc158.png)

이는 현재 가장 많은 데이터가 저장되어있는 arena에  데이터가 저장됨을 의미한다. 

#### 왜 가장 freepool이 많은 곳에 데이터가 저장되면 않될까? 

block이 free 상태이더라도 메모리가 즉시 해제되는 것이 아니기 때문이다. Python process는 해당 메모리를 할당한 상태로 유지하고 새로운 데이터를 할당하기 위해 재사용 한다. Python에서는 진정으로 메모리가 해제될수 있는 대상은 Arena이기 때문에, Arena는 최대한 empty상태를 유지해야 한다. 이런 방식으로 메모리들은 진정으로 해제 될수 있으며, 전체적으로 memory footprint가 감소하게 된다.

## [출처](https://realpython.com/python-memory-management/)