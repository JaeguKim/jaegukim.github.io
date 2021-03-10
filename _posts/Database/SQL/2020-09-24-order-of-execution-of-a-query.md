---
layout: post
title: "Order of execution of a Query (쿼리의 실행순서)"
date: 2020-09-24 +0900
categories: [Database,SQL]
---

# Query order of execution (쿼리의 실행순서)
1. **FROM, JOIN**
- subquery 포함가능, 임시 테이블들 생성가능

2. **WHERE**
- WHERE constraints에 적용되지 않는 rows 제거,
- FROM clause에 있는 칼럼들에 접근가능
- SELECT에 있는 Aliases에는 접근 불가 (SELECT문은 아직 실행이 안된 상태이기 때문에)

3. **GROUP BY**
- GROUP BY clause에 명시된 공통값들로 그룹화 됨
- aggregate function들을 사용할때만 사용

4. **HAVING**
- 그룹화된 행들을 대상으로 constraint 적용
aliases은 역시 사용불가능

5. **SELECT**

6. **DISTINCT**
- 명시된 Column에 대하여 중복된 값을 가진 행들을 제거

7. **ORDER BY**
- 오름차순 or 내림차순으로 행들을 정렬
- SELECT에 명시된 aliases에 접근가능

8. **LIMIT / OFFSET**
- LIMIT,OFFSET 키워드로 명시된 범위에 속하지 않는 행들 제거
- LIMIT : 몇개 추출할것인가
- OFFSET : 몇번째 ROW 부터 포함시킬 것인가 (zero based index), 0이면 생략가능
Example : LIMIT 2 OFFSET 1 (1,2 행을 추출)
