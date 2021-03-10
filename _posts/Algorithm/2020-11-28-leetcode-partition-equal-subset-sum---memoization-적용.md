---
layout: post
title: "[Leetcode] Partition Equal Subset Sum - memoization 적용"
date: 2020-11-28 11:29:00 +0900
categories: [Algorithm]
use_math: true
---

FANG에서 출제된 문제는 보기보다 간단한 경우가 많은것 같다. 처음에는 backtracking으로 접근을 하긴 했지만 시간복잡도가 O($2^N$)이기 때문에 접근을 포기했다. DP로 풀자니 어떤 부분을 subproblem으로 나눠야 하는지 잘 보이지 않았고, 더 오래 고민했으면 풀수도 있었을것 같다.

다음은 Top down DP로 풀이한 코드이다.

``` java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int num : nums){
            total += num;
        }
        if (total % 2 != 0){
            return false;
        }

        return canPartition(nums,total,0,0,new HashMap<>());
    }

    public boolean canPartition(int[] nums, int total, int index, int sum, Map<String,Boolean> map) {
        String key = String.format("%d|%d",index,sum);
        if (index >= nums.length || sum > total/2) {
            return false;
        }
        if (map.containsKey(key)){
            return map.get(key);
        }
        if (sum * 2 == total) { 
            return true;
        }
        boolean result = canPartition(nums,total,index+1,sum+nums[index],map) || canPartition(nums,total,index+1,sum,map);
        map.put(key,result);
        return result;
    }
}
```

위 부분에서 놓치기 쉬운 부분은 이 부분인것 같다.
``` java
if (index >= nums.length || sum > total/2) {
        return false;
    }
```

sum가 total/2 보다 클때 함수를 리턴하지 않으면 결국은 TLE 가 나기 때문이다.

위의 시간복잡도는 O(N * M), N : 인풋크기
M : 원소의 총합 / 2

