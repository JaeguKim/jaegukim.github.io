---
layout: post
title: "Jupyter Notebook에 hive-site.xml 마운트하기"
date: 2021-08-16 23:31:00 +0900
categories: [Kubernetes]
---

Jupyter Notebook은 hive metastore에 접근하기 위해서, ```/opt/spark/conf/``` 경로에 ```hive-site.xml``` 이 필요하다.

## Secret에 있는 hive-site.xml을 마운트하기

hive-site.xml에는 metastore 접속 패스워드가 있어, 이를 configMap에 포함하면 위험하다. 따라서 Secret에서 읽어오는 것이 좋다.

[다음 링크](https://zero-to-jupyterhub.readthedocs.io/en/latest/jupyterhub/customizing/user-storage.html#additional-storage-volumes) 를 참고하여, Secret에 있는 hive-site.xml을 마운트 할 수 있다.

다음 예제를 조금 수정하면 된다.

``` yaml
singleuser:
  storage:
    extraVolumes:
      - name: jupyterhub-shared
        persistentVolumeClaim:
          claimName: jupyterhub-shared-volume
    extraVolumeMounts:
      - name: jupyterhub-shared
        mountPath: /home/shared
```

``` yaml
singleuser:
  storage:
    extraVolumes:
      - name: metastore-secret
        secret:
          secretName: notebook-dev-xtrm-data-io
    extraVolumeMounts:
      - name: metastore-secret
        mountPath: /opt/spark/conf/hive-site.xml
        subPath: hive-site.xml
```

원래는 singleuser 외부 property에 다음처럼 정의 했는데, mount가 잘 되지 않았다. 아마 storage property가 이미 존재해서 인것 같다. 

``` yaml
extraVolumes:
    - name: metastore-secret
    secret:
        secretName: notebook-dev-xtrm-data-io
extraVolumeMounts:
    - name: metastore-secret
    mountPath: /opt/spark/conf/hive-site.xml
    subPath: hive-site.xml
```