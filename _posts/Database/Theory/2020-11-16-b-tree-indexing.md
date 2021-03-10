---
layout: post
title: "B-Tree Indexing"
date: 2020-11-16 19:55:00 +0900
categories: [Database,Theory]
---

# B-Tree란 무엇인가?
B-tree는 정열된 순서로 데이터를 저장할때 사용하는 자료구조이다. 샘플 B-tree는 다음과 같다.

![b-tree](https://cdn-images-1.medium.com/max/1600/1*pE4SEz7CprzFd7Zww-axfQ.jpeg)

[출처](https://dzone.com/articles/database-btree-indexing-in-sqlite)

각각의 노드에 키값들은 두개의 reference를 가지고 있으며, 각각의 reference는 다른 자식노드를 가리킨다. 왼쪽에 위치한 자식노드는 현재 키 값보다 작으며, 오른쪽에 위치한 자식노드는 현재 키 값보다 크거나 같다. 

# DB에서 인덱싱을 사용하는 이유

| Type | Insertion | Deletion | Lookup
| ---- | --- | --- | --- 
|Unsorted Array | O(1) | O(n) | O(n)
|Sorted Array | O(n) | O(n) | O(log(n))
|B-tree | O(log(n)) | O(log(n)) | O(log(n))

Binary Tree알고리즘을 이용하면 검색이 빨라지는데, B-tree는 Binary Tree의 일반화된 형태이다.
위 표에서 보듯이, B-tree를 사용하면 삽입,삭제,읽기가 log(n)안에 가능하다.
B-tree는 노드당 하나의 entry만 가지는 대신, 여러개의 entry를 갖는다. 그리고 각각의 entry는 자식노드를 갖는다.

# B-tree vs B-tree
B-tree는 인덱싱을 하기위해서 사용되고, B+tree는 데이터를 저장하기 위해서 사용하는 data structure이다. 

![B+tree](https://cdn-images-1.medium.com/max/1600/1*6I4SEl4K-twbuHUFNSw_7Q.jpeg)

[출처](https://dzone.com/articles/database-btree-indexing-in-sqlite)

위에서 보듯이, non-leaf 노드들이 leaf-nodes에서 복제가 된것을 확인할수 있다. 
그리고 leaf 노드들은 모든 데이터를 포함하고 있고, 데이터들은 정렬되어있다. B+ tree를 사용하면 B-tree와 동일하게 탐색이 가능할뿐만 아니라, leaf node들을 아래와 같이 순회할수 있다.

![B+tree](https://cdn-images-1.medium.com/max/1600/1*-L5pwsqX-AjSiGkV0MPQVg.jpeg)

[출처](https://dzone.com/articles/database-btree-indexing-in-sqlite)

# DB에서 어떻게 사용되는가?
먼저, 데이터베이스는 unique random index(또는 primary key)를 각각의 데이터에 생성하고 관련 row들을 byte stream으로 변환한다. 그리고 key와 byte stream을 B+tree에 저장한다. 여기서 random index가 indexing을 위한 key로 사용된다. key와 record byte stream은 합쳐서 payload라고 부른다. 
결과 B+ tree는 아래와 같다.

![B+tree](https://cdn-images-1.medium.com/max/1600/1*LF6-glMyvdIiAk-JykIIXw.jpeg)

[출처](https://dzone.com/articles/database-btree-indexing-in-sqlite)

위에서 보듯이 B+tree의 leaf 노드들에 레코드들이 저장되있고, 인덱스가 B+tree를 만드는데 사용되었음을 알수 있다. 이제 데이터베이스는 index를 사용하여 이분탐색하거나 leaf 노드들을 순회함으로써 sequential search를 할수 있다.

인덱싱이 사용되면, 데이터베이스는 B-tree를 생성하고, 각각의 index는 실제데이터를 가리킨다.

![B-tree](https://cdn-images-1.medium.com/max/1600/1*pXI0w1RagRCixnVnDysQvg.jpeg)

[출처](https://dzone.com/articles/database-btree-indexing-in-sqlite)

인덱싱이 처음에 사용되면, 데이터베이스는 주어진 키를 B-tree에서 탐색하고 index를 O(log(n)) 만에 얻는다. 그리고 나서, 그 index를 사용하여 B+tree를 탐색하고 O(log(n))에 데이터를 찾는다.

B-tree와 B+tree에 있는 노드들은 Page에 저장되는데, Page는 고정된 크기를 가지고 있다. Page들은 unique한 숫자를 가지고 있고, page는 다른 page를 가리킬수 있다. page의 사작부분에는 page meta detail 정보들(rightmost child page number, first free cell offset, first cell offset stored 등)이 저장되어있다.

데이터베이스에는 두가지 타입의 Page가 존재한다.

1. 인덱싱을 위한 Page : 이 페이지들은 오직 index와 다른 Page의 reference를 저장한다.

2. 레코드들을 위한 Page : 이 페이지들은 실제 데이터를 저장하고 leaf page여야만 한다.

# 결론
B-tree는 insert와 read를 하는데 있어서 효율적인 방법을 제공한다. 실제 데이터베이스 구현에서는 B-tree(indexing하기 위해서)와 B+tree(데이터 저장을 위해서)를 모두 사용한다.

[출처 : https://dzone.com/articles/database-btree-indexing-in-sqlite](https://dzone.com/articles/database-btree-indexing-in-sqlite)