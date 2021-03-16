---
layout: post
title: "Trouble Shooting"
date: 2020-12-26 20:15:00 +0900
categories: [DataEngineering,Spark]
---

## '''spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 MongoSpark.py''' 실행시 

### 에러

'''
java.lang.NoSuchMethodError: org.apache.spark.sql.catalyst.analysis.TypeCoercion$.findTightestCommonTypeOfTwo()Lscala/Function2;
'''

### 해결방법

```
spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.2.0 MongoSpark.py
```


