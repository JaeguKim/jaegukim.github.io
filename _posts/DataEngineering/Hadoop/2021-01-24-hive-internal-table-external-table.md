---
layout: post
title: "Hive Internal table, External table"
date: 2021-01-24 15:05:00 +0900
categories: [DataEngineering,Hadoop]
---

## Internal Table

Hive에서 디폴트로 테이블을 생성하면, Internal table로 생성이 되고, 이를 **Managed table**이라고도 부른다. internal table들이 생성한 모든 데이터베이스들은 디폴트로 hdfs의  ```/user/hive/warehouse``` 경로에 저장된다. 디폴트 저장 허브를 **hive.metastore.warehouse.dir** 에서 변경할수 있다. Internal table(Managed table)들을 drop하게 되면, 모든 메타데이터와 테이블 데이터들이 hdfs에서 영구적으로 삭제된다. Hive외부에서 데이터가 이용되어야 하거나, hdfs상의 다른 하둡 유틸리티들에 의해서 사용되어야한다면, external table을 고려해야한다.

### Internal table에 대한 키포인트

- Hive는 테이블 데이터를 ```database-name/table-name```으로 로드한다.
- Internal table은 ```TRUNCATE``` 커멘드를 지원한다.
- ACID를 지원한다.
- 쿼리 결과 캐싱을 지원한다. 즉,이미 실행된 hive 쿼리에 대한 결과를 저장한다.
- 테이블이 drop되면, 메타데이터와 테이블 데이터는 둘다 삭제된다.

### 데모

**Step 1** : 테이블 생성

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224163924/createtabletest.png)



**Step 2** : 테이블 test에 데이터 로드

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224163948/loaddatatotest.png)



**Step 3** : test 테이블 데이터 조회

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224170623/selecttest.png)



**Step 4** : 테이블 describe

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224164426/describeextendedtest.png)



**Step 5** : 테이블 truncate

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224164605/truncatetabletest.png)



**Step 6** : drop 테이블

![img](https://media.geeksforgeeks.org/wp-content/uploads/20201224170640/droptabletest.png)



## External Table

Hive는 external table에 저장된 데이터에 대한 소유권이 없다. 사용자가 external table을 drop하면 오직 데이블의 메타데이터만 삭제되고 데이터는 안전하다. **CREATE EXTERNAL**키워드를 사용하여 생성하게 되고 데이터가 저장되어 있는 hdfs위치도 명시해야한다. external table에 대한 메타데이터는 hive가 관리하고, 테이블 데이터는 hdfs상의 다른 경로에 저장된다.

### External table에 대한 keypoint

- Hive는 warehouse로 데이터를 가져오지 않는다.
- External table은 TRUNCATE 커멘드를 지원하지 않는다.
- ACID 트렌젝션 성질을 지원하지 않는다.
- query result 캐싱을 지원하지 않는다.
- external table이 drop되면 오직 메타데이터만 삭제된다.

### 데모

아래 링크 참고



## 출처 

[https://www.geeksforgeeks.org/difference-between-hive-internal-and-external-tables/?ref=rp](https://www.geeksforgeeks.org/difference-between-hive-internal-and-external-tables/?ref=rp)