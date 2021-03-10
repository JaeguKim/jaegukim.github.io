---
layout: post
title: "[Leetcode] Smallest Integer Divisible by K"
date: 2020-11-26 12:03:00 +0900
categories: [Algorithm]
---

위 문제에 수열이 1,11,111,1111,... 이므로 다음 식이 성립한다.

``` next = prev * 10 + 1 ```

이 문제의 핵심은 다음수와 현재수 사이에 모듈러 관계를 파악하는 것이다.

결론적으로 말하면 모듈러 관계는 다음과 같다.

```
A = prev % K
B = next % K = (A*10 + 1) % K 
``` 

이제 위식을 좀더 풀어 쓰면 다음과 같다.

```
B = next % K
= (prev * 10 + 1) % K
= ((prev * 10) % K + 1 % K) % K
= ((prev % K) * (10 % K) + 1 % K) % K
= (A * (10 % K) + 1 % K) % K
= (A * 10 + 1)%K
```

결론적으로, 이전 나머지에서 그다음 항의 나머지를 구하고, 나머지에서 cycle이 발견되거나 0이 발견될때까지 이를 반복하는 방식으로 구현하였다.

``` java
import java.util.HashSet;
import java.util.Set;

class Solution { 
    public int smallestRepunitDivByK(int K) {
        Set<Integer> set = new HashSet<>();
        int rem = 1%K;
        int len = 1;
        while (rem != 0 && !set.contains(rem)){
            set.add(rem);
            rem = (rem*10+1)%K;
            len += 1;
        }

        if (rem == 0){
            return len;
        }
        else {
            return -1;
        }
    }
}
```