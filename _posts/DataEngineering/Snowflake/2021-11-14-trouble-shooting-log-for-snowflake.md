---
layout: post
title: "Trouble shooting log for snowflake"
date: 2021-11-14 15:03:00 +0900
categories: [DataEngineering,Snowflake]
---

## 2021.11.09
- 문제상황 : 기존에 RDS에 적재되고 있는 데이터를 Snowflake warehouse로 적재하는 batch job을 구현했었는데, 과거 데이터들 또한 snowflake에 적재하는 backfill 작업을 수행해야 할일이 있었다. s3에 데이터를 저장하는 backfill작업은 airflow상에서 진행했지만 문제는 지난 데이터들을 snowflake external table에서 바라볼수 있도록 `ALTER TABLE {table_name} REFRESH {stage_path to refresh}` 커멘드를 실행해야하는데, 데이터가 저장되는 stage_path가 특정 날짜 경로(예를들어 `/dt=2021-11-01`)안에서 여러 종류의 디렉토리로 나누어지고 각각의 디렉토리가 독립적인 external table에서 사용되는 데이터가 저장되어있어서 백필할 모든 날짜에 대해서 아래 커멘드를 실행해야하는 번거로운 상황이 발생했다.

- external_table_1 의 경우 : `ALTER TABLE ad_groups_table REFRESH "dt=2021-11-01/ad_groups"`

- external_table_2 의 경우 : `ALTER TABLE campaign_table REFRESH "dt=2021-11-01/campaign.json"`

- external_table_3의 경우 : `ALTER TABLE creative_set_table REFRESH "dt=2021-11-01/creative_sets"`

현재 백필해야하는 지난 5개월동안의 데이터에 대해서, 각각의 날짜에 대해서 위의 커멘드를 실행하는 python script를 실행해야하나 하는 고민이 되었다. 하지만 external table 생성시 `PATTERN` 속성을 활용하면 이러한 문제를 쉽게 해결할수 있다.

PATTERN은 external table에 mapping할 파일들의 full path에 대해서 regex를 적용하여, 특정 파일들만 external table에 mapping할수 있다.

- external_table_1의 경우 : `PATTERN='.*ad_groups.*[.]json`

- external_table_2의 경우 : `PATTERN='.*campaign.*[.]json`

- external_table_3의 경우 : `PATTERN='.*creative_sets.*[.]json`

따라서 기존의 테이블들을 drop하고 위 옵션을 추가하여 테이블을 재 생성하였다. 재생성할때 `REFRESH_ON_CREATE` 값을 true로 설정하여 바로 파일들이 맵핑이 되도록 할 수 있다.


