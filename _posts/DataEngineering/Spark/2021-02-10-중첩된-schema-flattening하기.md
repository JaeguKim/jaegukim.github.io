---
layout: post
title: "중첩된 schema flattening하기"
date: 2021-02-10 09:56:00 +0900
categories: [DataEngineering,Spark]
---

``` scala
def flattenSchema(schema: StructType, prefix: String = null): Array[Column] = {
    schema.fields.flatMap(f => {
      val colName = if (prefix == null) f.name else (prefix + "." + f.name)
      f.dataType match {
        case st: StructType => flattenSchema(st, colName)
        case _ => Array(col(colName) as colName)
      }
    })
}
```

## 출처 
[https://stackoverflow.com/questions/37471346/automatically-and-elegantly-flatten-dataframe-in-spark-sql/37473765#37473765](https://stackoverflow.com/questions/37471346/automatically-and-elegantly-flatten-dataframe-in-spark-sql/37473765#37473765)