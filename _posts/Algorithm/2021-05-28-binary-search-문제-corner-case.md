---
layout: post
title: "Binary Search 문제 corner case"
date: 2021-05-28 11:39:00 +0900
categories: [Algorithm]
---

[Leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)이 문제는 전형적인 바이너리 서치 문제이다. 이 문제에서 실수할 만한 코너 케이스가 있다. 

``` java
class Solution {
    public int findMin(int[] nums) {
        int ans = nums[0];
        int l = 0, r = nums.length-1;
        while (l <= r) {
            int mid = (l+r)/2;
            ans = Math.min(nums[mid],ans);
            if (nums[mid] > nums[0]) l = mid+1;
            else r = mid-1;
        }
        return ans;
    }
}
```
위 코드에서 [2,1]이 입력으로 들어온다면, 1은 체크를 할수 없게 된다. 결과적으로 오답으로 처리가 된다.
``` if (nums[mid] >= nums[0]) ``` 로 수정하니 정답은 나오지만, 이러한 경우가 발생할 수 있다는 사실을 염두해둬야 겠다.