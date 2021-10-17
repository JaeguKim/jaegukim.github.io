---
layout: post
title: "command(MongoDB)"
date: 2021-10-05 22:43:00 +0900
categories: [Database,MongoDB]
---

## login with root user
```sh
$ mongo
>> use admin
>> db.auth("username", "password")
```

## Drop all databases except for internal collections
``` sh
db
  .getMongo()
  .getDBNames()
  .filter(n => !['admin','local','config'].includes(n))
  .forEach(dname =>
    db
      .getMongo()
      .getDB(dname)
      .dropDatabase()
  )
;
```

