---
layout: post
title: "Trouble Shooting"
date: 2021-09-02 22:45:00 +0900
categories: [AWS]
---

## sts:assumeRoleWithWebIdentity problem
service account가 바인딩되어 있는 role의 assume role에 OIDC provider 설정이 안되어있을때 발생!
[설정방법](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html)

## efs-csi-driver사용시 dynamic provisioned pvc에 대해서 chown/chgrp 이 불가능한 문제
chown, chgrp 제거
[참고](https://github.com/kubernetes-sigs/aws-efs-csi-driver/issues/300)