---
layout: post
title: "Trouble Shooting(Terraform)"
date: 2022-05-26 13:38:00 +0900
categories: [Terraform]
---

## `Terraform plan`시 `Error: Failed to query available provider packages`
발생원인 : azure 리소스를 정의할때 모듈명을 `azurerm_...` 로 명시했어야 됬는데, `azurem_...` 으로 명시했을때 문제가 발생했음.
