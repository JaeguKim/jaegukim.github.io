---
layout: post
title: "Trouble shooting log(Airflow)"
date: 2021-10-17 12:00:00 +0900
categories: [DataEngineering,Airflow]
---

## Trouble Shooting

### DB Creation and initialization failed
```[2020-12-08 11:19:30,734] {manager.py:96} ERROR - DB Creation and initialization failed: Invalid argument(s) 'pool_size','max_overflow' sent to create_engine(), using configuration SQLiteDialect_pysqlite/StaticPool/Engine.  Please check that the keyword arguments are appropriate for this combination of components.```

airflow.cfg에 다음 라인 추가

```
[webserver]
rbac = True
```

### airflow initdb: undefined symbol: Py_GetArgcArgv
change python version larger than 3.8.5 [link](https://stackoverflow.com/questions/60684146/airflow-initdb-undefined-symbol-py-getargcargv)

### `OSError: mysql_config not found`
docker 이미지 빌드시 `pip install` 하기전에 다음을 실행
`apt-get install libmysqlclient-dev`

### `fatal error: Python.h:`
dockerfile에 현재 사용하고 있는 python 버전에 맞는 dev패키지 설치
```
    sudo apt-get install python3.x-dev  # for python3.x installs
```

## airflow backfill command 버그 
가끔 다음의 backfill command가 동작하지 않을때가 있다. backfill이 완료되었다고는 뜨는데 실제로 데이터가 백필이 되지 않은경우가 발생되었다. 당시 특정 날짜에만 이런 현상이 발생해서 혼란스러웠다.
`airflow tasks test`(eg. `airflow tasks test hourly_third_party load_apple_ads_api_to_s3 2021-10-09`) 커멘드를 사용해서 특정 테스크를 실행해서 이런 현상을 해결했다.