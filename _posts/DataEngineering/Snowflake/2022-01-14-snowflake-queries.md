---
layout: post
title: "[Snowflake] Queries"
date: 2022-01-14 15:00:00 +0900
categories: [DataEngineering,Snowflake]
---

## cancel query

- by query id : ```select system$cancel_query('d5493e36-5e38-48c9-a47c-c476f2111ce5'); ```

- by session id : ```select system$cancel_all_queries(1065153872298);```

