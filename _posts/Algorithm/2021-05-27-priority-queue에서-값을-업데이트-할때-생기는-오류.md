---
layout: post
title: "[Leetcode - LRU Cache] Priority Queue에서 값을 업데이트 할때, 생길수 있는 오류"
date: 2021-05-27 12:26:00 +0900
categories: [Algorithm]
---

리트코드에서 [LRU Cache](https://leetcode.com/problems/lru-cache/) 문제를 풀때, 한시간넘게 디버깅한 적이있다. 즉, PriorityQueue에 저장된 객체의 값을 업데이트 할때, ```heapify``` 과정이 자동으로 일어난다고 생각했기 때문이다. 

``` java
    public int get(int key) {
        if (map.containsKey(key)) {
            Info info = map.get(key);
            info.t = ++time;
            return info.value;
        }
        else return -1;
    }

     public void put(int key, int value) {
        if (!map.containsKey(key) && map.size()+1 > capacity && pq.size() > 0) {
            map.remove(pq.poll().key);
        }
        if (map.containsKey(key)) {
            Info info = map.get(key);
            info.value = value;
            info.t = ++time;
        }
        else {
            Info newInfo = new Info(key,value);
            newInfo.t = ++time;
            map.put(key,newInfo);
            pq.add(newInfo);
        }
    }
```

만약 위와 같이 함수를 정의한다면, PriorityQueue에 저장된 객체의 값이 변경되더라도, ```poll()``` 을 호출했을때 올바른 객체가 리턴되지 않는다. 왜냐하면 객체의 값이 변경된 시점에 ```heapify``` 과정이 일어나지 않았기 때문이다. 이를 바로 잡기 위해서는 아래와 같이 ```Info``` 객체를 삭제하고 다시 삽입하는 과정을 거쳐야한다. 바로 아래처럼 말이다.

``` java
    public LRUCache(int capacity) {
        map = new HashMap<>();
        this.capacity = capacity;
        pq = new PriorityQueue<>();
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            Info info = map.get(key);
            info.t = ++time;
            pq.remove(info);
            pq.add(info);
            return info.value;
        }
        else return -1;
    }

    public void put(int key, int value) {
        if (!map.containsKey(key) && map.size()+1 > capacity && pq.size() > 0) {
            map.remove(pq.poll().key);
        }
        if (map.containsKey(key)) {
            Info info = map.get(key);
            info.value = value;
            info.t = ++time;
            pq.remove(info);
            pq.add(info);
        }
        else {
            Info newInfo = new Info(key,value);
            newInfo.t = ++time;
            map.put(key,newInfo);
            pq.add(newInfo);
        }
    }
```