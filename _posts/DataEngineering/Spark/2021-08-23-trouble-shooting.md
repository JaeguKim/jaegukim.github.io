---
layout: post
title: "Trouble Shooting"
date: 2021-08-23 22:43:00 +0900
categories: [DataEngineering,Spark]
---

```
java.io.InvalidClassException: org.apache.spark.resource.ResourceProfile; local class incompatible: stream classdesc serialVersionUID = 7048704245620002090, local class serialVersionUID = -2817202060116599060
...
```

[주로 Spark Version을 두가지 섞어쓸때 발생한다고 한다.](https://community.cloudera.com/t5/Support-Questions/Spark-Standalone-error-local-class-incompatible-stream/td-p/25909) 

실제 업무에서는 spark configuration을 설정시 ```spark.kubernetes.container.image``` 부분에 3.0.0 버전을 사용하였는데, 실제 Spark Operator는 3.1.1 버전이라서 에러가 발생했다. spark 이미지를 3.1.1로 수정하니 잘 되었다.
