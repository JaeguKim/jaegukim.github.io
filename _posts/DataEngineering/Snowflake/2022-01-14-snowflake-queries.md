---
layout: post
title: "[Snowflake] Queries"
date: 2022-01-14 15:00:00 +0900
categories: [DataEngineering,Snowflake]
---

## cancel query

- by query id : ```select system$cancel_query('d5493e36-5e38-48c9-a47c-c476f2111ce5'); ```

- by session id : ```select system$cancel_all_queries(1065153872298);```

## Get First Row of each group

```
SELECT NAME,DEPT,SALARY
FROM (SELECT *, ROW_NUMBER () OVER(PARTITION BY DEPT ORDER BY SALARY DESC) AS rn
FROM employee
) WHERE rn = 1;
```

- [참고](https://dwgeek.com/how-to-get-first-row-of-each-group-in-snowflake.html/)

## Add column to table

```
ALTER TABLE prod.server.matching_user_wait_duration_seconds_sum ADD COLUMN play_type STRING;
```
