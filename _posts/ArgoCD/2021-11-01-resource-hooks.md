---
layout: post
title: "Resource Hooks"
date: 2021-11-01 15:34:00 +0900
categories: [ArgoCD]
---

## Hook types

| `PreSync`  | Executes prior to the application of the manifests.          |
| ---------- | ------------------------------------------------------------ |
| `Sync`     | Executes after all `PreSync` hooks completed and were successful, at the same time as the application of the manifests. |
| `Skip`     | Indicates to Argo CD to skip the application of the manifest. |
| `PostSync` | Executes after all `Sync` hooks completed and were successful, a successful application, and all resources in a `Healthy` state. |
| `SyncFail` | Executes when the sync operation fails. *Available starting in v1.2* |