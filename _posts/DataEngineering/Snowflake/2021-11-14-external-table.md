---
layout: post
title: "External table"
date: 2021-11-14 14:53:00 +0900
categories: [DataEngineering,Snowflake]
---

## External Table
external table의 실제 데이터는 external stage에 있는 파일들에 저장이 되어 있다. External table들은 data file들에 대한 file-level metadata를 저장하고 있다. (such as filename, a version identifier, related properties) External table들은 read-only이지만 join또한 가능하다. View또한 external table을 대상으로 만들어 질수 있다. DB에 있는 데이터보다 쿼리속도는 느리지만 materialized view를 만들어서 성능을 향상 시킬수 있다. 

## [출처](https://docs.snowflake.com/en/user-guide/tables-external-intro.html)