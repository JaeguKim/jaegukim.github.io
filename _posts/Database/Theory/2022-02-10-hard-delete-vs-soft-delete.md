---
layout: post
title: "Hard Delete vs Soft Delete"
date: 2022-02-10 12:12:00 +0900
categories: [Database,Theory]
---

## Delete type

Hard Deletes란 테이블에서 레코드가 삭제되면, 해당 레코드는 물리적으로도 삭제가 되는것을 의미한다.

Soft Deletes란 테이블에서 레코드가 삭제되었다고 하더라도, 물리적으로는 삭제가 되지 않는다. 하지만 테이블에 있는 필드가 해당 레코드가 삭제되었음을 알려준다. 해당 필드는 `is_deleted` 또는 `deleted_timestamp`와 같이 boolean 값을 가질수 있다.

## Hard Delete를 사용해야 하는 경우

만약 soft delete방식을 사용할 경우, company_revenue 테이블에 ```select count(revenue) from company_revenue```  라고 쿼리했을때 revenue 합이 잘못 집계가 될수 있으므로 **analytic data warehouse** 의 경우에는 hard delete를 사용하는것이 좋다.



## Soft Delete를 사용해야 하는 경우

ETL과정에서 incremental extraction을 해야하는 경우, 삭제된 row를 식별해야하는 경우 Soft delete를 사용해야 한다.



아래 예시를 보자.



| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason          | Last_modified_timestamp |
| ------ | -------- | -------------------- | ------------------------------- | ----------------------- |
| 1      | Mac      | 2019-12-17           | Ate thread from a sewing bucket | 2019-12-18              |
| 2      | Cheese   | 2018-12-01           | Ate hair elastics               | 2018-12-02              |
| 3      | Sushi    | 2019-12-18           | Neutering                       | 2019-12-19              |

만약 2019년 12월 20일에 하루전 변경된 레코드를 추출하면 다음 한개의 row를 얻을 것이다.

| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason | Last_modified_timestamp |
| ------ | -------- | -------------------- | ---------------------- | ----------------------- |
| 3      | Sushi    | 2019-12-18           | Neutering              | 2019-12-19              |

그리고 12월 20일에 테이블이 아래와 같이 업데이트 되었다고 가정하자. 아래 테이블을 살펴보면 cat_id가 2인 레코드가 삭제되고 5인 레코드가 다시 삽입된것을 확인할 수 있다.

| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason          | Last_modified_timestamp |
| ------ | -------- | -------------------- | ------------------------------- | ----------------------- |
| 1      | Mac      | 2019-12-17           | Ate thread from a sewing bucket | 2019-12-18              |
| 2      | Cheese   | 2018-12-01           | Ate hair elastics               | 2018-12-02              |
| 5      | Tuna     | 2019-12-19           | Neutering                       | 2019-12-20              |

하루가 지난 12월 21일에 하루전 변경된 레코드를 추출하면, 아래와 같이 삭제된 row는 추출할수가 없다.

| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason | Last_modified_timestamp |
| ------ | -------- | -------------------- | ---------------------- | ----------------------- |
| 5      | Tuna     | 2019-12-19           | Neutering              | 2019-12-20              |

이때 Soft Delete를 사용하면 문제를 해결할수 있다. Soft Delete를 사용시, 원본 테이블은 아래와 같을 것이다.

| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason          | Last_modified_timestamp | Is_deleted |
| ------ | -------- | -------------------- | ------------------------------- | ----------------------- | ---------- |
| 1      | Mac      | 2019-12-17           | Ate thread from a sewing bucket | 2019-12-18              | N          |
| 2      | Cheese   | 2018-12-01           | Ate hair elastics               | 2018-12-02              | N          |
| 3      | Sushi    | 2019-12-18           | Neutering                       | 2019-12-20              | Y          |
| 5      | Tuna     | 2019-12-19           | Neutering                       | 2019-12-20              | N          |

하루가 지난 12월 21일에 하루전 변경된 레코드를 추출하면, 아래와 같이 20일에 업데이트된 row를 정확하게 찾을 수 있다.

| Cat_id | cat_name | Hospitalization_date | Hospitalization_reason | Last_modified_timestamp | is_deleted |
| ------ | -------- | -------------------- | ---------------------- | ----------------------- | ---------- |
| 3      | Sushi    | 2019-12-18           | Neutering              | 2019-12-20              | Y          |
| 5      | Tuna     | 2019-12-19           | Neutering              | 2019-12-20              | N          |

참고로 이 시점에, Snowflake에서 아래처럼 merge statement를 사용해서, 데이터를 복제할 수 있다.

``` sql
MERGE INTO cat_hospitalization_fact as t
USING source_data as s
ON t.cat_id = s.cat id
AND t.hospitalization_date = s.hospitalization_date
WHEN MATCHED THEN UPDATE SET
t.cat_name  = s.cat_name,
t.hospitalization_reason = s.hospitalization_reason,
WHEN NOT MATCHED THEN INSERT
(cat_id, cat_name, hospitalization_reason, hospitalization_date)
VALUES 
(s.cat_id, s.cat_name, s.hospitalization_reason, s.hospitalization_date)
WHEN MATCHED AND s.is_delete = ‘Y’ THEN DELETE
```



## 참고

[A Good Day to Delete Hard](https://medium.com/analytics-vidhya/a-good-day-to-delete-hard-22b8be83b622)

