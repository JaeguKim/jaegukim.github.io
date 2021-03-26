---
layout: post
title: "Data warehouse, Data Lake"
date: 2021-03-26 12:13:00 +0900
categories: [DataEngineering,Concept]
---

## Data Warehouse

> 정보의 중앙 저장소,분석방법을 포함한 정보 관리 시스템

## Data Lake

> structured,unstructured 데이터를 저장하기 위한 중앙 저장소. 데이터를 가공없이 있는 그대로 저장하여 대시보드와 시각화에서부터 벡데이터 처리, 실시간 분석, 머신러닝까지 수행할수 있다.

## Data Warehouse vs Data Lake

|    Characteristics    |                        Data Warehouse                        |                          Data Lake                           |
| :-------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|       **Data**        | Relational from transactional systems, operational databases, and line of business applications | Non-relational and relational from IoT devices, web sites, mobile apps, social media, and corporate applications |
|      **Schema**       |  Designed prior to the DW implementation (schema-on-write)   |       Written at the time of analysis (schema-on-read)       |
| **Price/Performance** |       Fastest query results using higher cost storage        |     Query results getting faster using low-cost storage      |
|   **Data Quality**   | Highly curated data that serves as the central version of the truth |    Any data that may or may not be curated (ie. raw data)    |
|       **Users**       |                      Business analysts                       | Data scientists, Data developers, and Business analysts (using curated data) |
|     **Analytics**     |            Batch reporting, BI and visualizations            | Machine Learning, Predictive analytics, data discovery and profiling |