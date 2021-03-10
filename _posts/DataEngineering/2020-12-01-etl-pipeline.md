---
layout: post
title: "ETL Pipeline"
date: 2020-12-01 17:22:00 +0900
categories: [DataEngineering]
---

# ETL Pipeline

ETL Pipeline이란 input source로 부터 데이터를 추출하고(extracting), 데이터를 변환하고, database, data mark, data warehouse에 저장하는 과정들을 말한다.

![image](https://databricks.com/wp-content/uploads/2019/02/etl.jpg) 

[출처](https://databricks.com/wp-content/uploads/2019/02/etl.jpg)

Extract, Transform, Load 의 약자이다.

## Extract

데이터는 다양한 source로 부터 추출될수 있다. 데이터는 구조화되어있을 수도 있지만 그렇지 않을수도 있다. 

## Transform

데이터를 다양한 application에서 사용될수 있도록 포맷을 변환하는 과정을 말한다.

## Load

일정한 포맷으로 변환된 데이터는 이제 저장된다.