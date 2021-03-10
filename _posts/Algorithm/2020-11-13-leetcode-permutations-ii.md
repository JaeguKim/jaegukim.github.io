---
layout: post
title: "[Leetcode] Permutations II"
date: 2020-11-13 11:33:00 +0900
categories: [Algorithm]
---

처음 내가 푼 방식은 다음과 같다.
1. hashMap에 0~n-1(n은 인풋갯수)범위 숫자를 저장
2. deque에 숫자의 인덱스값을 추가, 그리고 해당 idx가 추가되었으므로 hashMap에 해당 인덱스를 삭제한다.
3. deque가 인풋으로 들어온 숫자의 갯수와 일치하면 순열을 표현하는 문자열을 만들고 그것과 기존에 추가했던 순열정보와 중복되었는지 비교한다. 중복이 되지않았으면 deque에 있는 idx순서대로 인풋값을 새로운 list에 푸시한다.
최종적으로 새로운 list를 결과 배열에 푸시한다.

``` java
class Solution {
    Set<String> set;
    boolean[] visited;
    List<List<Integer>> res;
    
    public void dfs(int[] nums, Map<Integer, Integer> idxMap, Deque<Integer> deq) {
        if (deq.size() == nums.length) {
            Iterator<Integer> iter = deq.iterator();
            String s = "";
            List<Integer> list = new ArrayList<>();
            while (iter.hasNext()) {
                int idx = iter.next();
                s += Integer.toString(nums[idx])+"|";
                list.add(nums[idx]);
            }
            if (!set.contains(s)){
                set.add(s);
                res.add(list);
            }
            return;
        }

        Set<Integer> keys = idxMap.keySet();
        Iterator<Integer> iter = keys.iterator();
        List<Integer> idxList = new ArrayList<>();
        while (iter.hasNext()) {
            int idx = iter.next();
            idxList.add(idx);
        }
        for (int idx : idxList){
            idxMap.remove(idx);
            deq.add(idx);
            dfs(nums,idxMap,deq);
            deq.removeLast();
            idxMap.put(idx,1);
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        set = new HashSet<>();
        int n = nums.length;
        visited = new boolean[n];
        res = new ArrayList<>();
        Map<Integer,Integer> map = new HashMap<>();
        for (int i=0;i<n;i++){
            map.put(i,0);
        }
        dfs(nums,map,new ArrayDeque<>());
        return res;
    }
}
```

위 방식의 문제점은
1. deque는 뒤에서 숫자를 넣고 빼기에 특화된 자료구조가 아니다. stack이 적절한 자료구조이다. deque를 썼던 이유는 데이터를 뒤로 추가하기도 싶고 빼기도 쉬운 구조가 deque라고 생각해서 구현했는데, 생각해보면 앞으로 넣고 뺄일이 굳이 없는데 deque를 쓸 이유는 딱히 없었던 것이다.

2. deque에 있는 숫자 idx를 기준으로 결과 문자열을 만들고 이를 기존에 저장된 순열문자열과 비교하는것은 과정이 불편하다.

새로운 풀이에 대한 코드는 아래와 같다.
``` java
class Solution {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();

        // count the occurrence of each number
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (!counter.containsKey(num))
                counter.put(num, 0);
            counter.put(num, counter.get(num) + 1);
        }

        LinkedList<Integer> comb = new LinkedList<>();
        this.backtrack(comb, nums.length, counter, results);
        return results;
    }

    protected void backtrack(LinkedList<Integer> comb, Integer N, HashMap<Integer, Integer> counter,
            List<List<Integer>> results) {

        if (comb.size() == N) {
            // make a deep copy of the resulting permutation,
            // since the permutation would be backtracked later.
            results.add(new ArrayList<Integer>(comb));
            return;
        }

        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            Integer num = entry.getKey();
            Integer count = entry.getValue();
            if (count == 0)
                continue;
            // add this number into the current combination
            comb.addLast(num);
            counter.put(num, count - 1);

            // continue the exploration
            backtrack(comb, N, counter, results);

            // revert the choice for the next exploration
            comb.removeLast();
            counter.put(num, count);
        }
    }
}
```

## 개선된 점
- 이풀이는 unique한 숫자를 가지고 permutation을 만들기 때문에 set을 이용하여 지금까지 구한 수열리스트와 비교를 할 필요가 없다.
- ArrayList에 permutation결과를 저장하기 때문에 deque를 이용할때보다 최종 결과 배열에 permutation 결과값을 추가하기가 쉽다.

## 깨달은 점
**결국은 하나하나 이 라인이 왜 필요할까 생각하면서 코딩하는것이 중요하다는 사실을 깨달았다. 협업을 할때도 이러한 능력이 중요하지 않을까?**