---
layout: post
title:  "[LeetCode] Recover Binary Search Tree"
date:   2020-11-01
use_math: true
categories: [Algorithm]
---
먼저 이문제를 풀때 comparator함수를 작성할때 주의할점이 있다.
``` java
 sortedList.sort(new Comparator<TreeNode>() {
            @Override
            public int compare(TreeNode n1, TreeNode n2) {
                return n1.val - n2.val;
            }
        });
```
위와같이 작성했을때 $-2^{31}$ 에서 $2^{31}-1$ 이기 때문에 두수를 빼면 int 범위를 벗어나는 경우가 생긴다.
따라서 다음과 같이 작성해야한다.
``` java
sortedList.sort(new Comparator<TreeNode>() {
            @Override
            public int compare(TreeNode n1, TreeNode n2) {
                if (n1.val < n2.val) return -1;
                else if (n1.val == n2.val) return 0;
                else return 1;
            }
        });
```
다음은 시간복잡도 $Nlog{N}$ 풀이이다.
``` java
class Solution {

    private List<TreeNode> inorderList;
    void inorder(TreeNode root){
        if (root == null) return;
        inorder(root.left);
        inorderList.add(root);
        inorder(root.right);
    }

    public void makeOriginal(TreeNode root, int n1, int n2){
        if (root == null) return;
        makeOriginal(root.left, n1, n2);
        if (root.val == n1) root.val = n2;
        else if (root.val == n2) root.val = n1;
        makeOriginal(root.right, n1, n2);
    }

    public void recoverTree(TreeNode root) {
        inorderList = new ArrayList<>();
        inorder(root);
        List<TreeNode> sortedList = new ArrayList<>(inorderList);
        sortedList.sort(new Comparator<TreeNode>() {
            @Override
            public int compare(TreeNode n1, TreeNode n2) {
                if (n1.val < n2.val) return -1;
                else if (n1.val == n2.val) return 0;
                else return 1;
            }
        });
        int num1 = 0;
        int num2 = 0;
        for (int i=0; i<inorderList.size(); i++){
            if (inorderList.get(i).val != sortedList.get(i).val){
                num1 = inorderList.get(i).val;
                num2 = sortedList.get(i).val;
                break;
            }
        }
        makeOriginal(root, num1, num2);
    }
}
```

다음은 constant Space 풀이이다.
``` java
class Solution {
    TreeNode first = null;
    TreeNode second = null;
    TreeNode pre = null;
    public void recoverTree(TreeNode root) {
        travers(root);
        
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }
    public void travers(TreeNode node){
        if(node == null) return;
        travers(node.left);
        if(first == null && pre != null && pre.val >= node.val){
            first = pre;
        }
        if(first != null &&pre != null && pre.val >= node.val){
            second = node;
        }
        
        pre = node;
        travers(node.right);
    }
}
```