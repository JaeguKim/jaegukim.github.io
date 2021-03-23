---
layout: post
title: "PySpark UDF"
date: 2021-03-23 22:44:00 +0900
categories: [DataEngineering,Spark]
---

## PySpark UDF

- native Python 라이브러리와 Spark을 연동
- UDF는 독립적인 프로세스로 실행
- 데이터가 Python과 Java간에 전달됨

## PySpark UDF vs Pandas UDF

| Existing UDF | Pandas UDF
| Function on Row | Function on Row, Group and Window
| Pickle serialization | Arrow Serialization
| Data as Python objects | Data as pd.Series (for column) and pd.DataFrame (for table)

## Pandas UDF limitations

- must split data
- each group must fit entirely in memory

## 출처
[https://databricks.com/session/vectorized-udf-scalable-analysis-with-python-and-pyspark](https://databricks.com/session/vectorized-udf-scalable-analysis-with-python-and-pyspark)