---
layout: post
title: "[Hackerrank] Top Competitors"
date: 2020-10-01 +0900
categories: [Database,SQL]
---
``` sql
SELECT H.HACKER_ID, H.NAME
FROM HACKERS H, DIFFICULTY D, CHALLENGES C, SUBMISSIONS S
WHERE H.HACKER_ID = S.HACKER_ID AND D.DIFFICULTY_LEVEL = C.DIFFICULTY_LEVEL AND C.CHALLENGE_ID = S.CHALLENGE_ID AND S.SCORE = D.SCORE
GROUP BY H.HACKER_ID,H.NAME
HAVING COUNT(H.HACKER_ID) > 1
ORDER BY COUNT(H.HACKER_ID) DESC, H.HACKER_ID
```
`GROUP BY H.HACKER_ID, H.NAME` 대신 `GROUP BY H.HACERK_ID` 만 사용할시 다음의 에러를 볼수 있다.  

`ERROR 1055 (42000) at line 1: Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'run_lf9qo4ybaab.h.name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by`

SELECT에서 사용된 칼럼중 GROUP BY 절에있는 칼럼에 함수적 종속성을 가지고 있지 않은 칼럼이 있다는 뜻이다.

여기서 함수적 종속성이란?
어떤 릴레이션 R에서, X와 Y를 각각 R의 애트리뷰트 집합의 부분 집합이라 하자. 애트리뷰트 X의 값 각각에 대해 애트리뷰트 Y의 값이 오직 하나만 연관되어 있을 때 Y는 X에 함수 종속이라 하고, X → Y라고 표기한다.
즉, HACKER_NAME은 HACKER_ID에 함수적으로 종속적이지 않다.
