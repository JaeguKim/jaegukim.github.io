---
layout: post
title: "Adding jar or package to Spylon Kernel"
date: 2021-08-24 16:31:00 +0900
categories: [DataEngineering,JupyterNotebook]
---

``` 
%%init_spark
launcher.jars = ["/some/local/path/to/a/file.jar"]
launcher.packages = ["maven:coordinates"]
```

maven coordicates를 구성하는 방법은 ```[groupId]:[artifactId]:[version]``` 으로 구성하면된다.
예시는 다음과 같다.
```
%%init_spark
launcher.packages = ["org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1"]
```

## [SOURCE](https://github.com/vericast/spylon-kernel/issues/46)