---
layout: post
title: "[Python] Syntax"
date: 2021-12-19 14:15:00 +0900
categories: [Language,Python]
---

## Passing a dictionary to a function as keyword parameters
Use ** operator to unpack the dictionary
``` python
# example
d = dict(p1=1,p2=2)
def f2(p1,p2):
    print p1, p2
f2(**d)
```

## type casting
``` python
# cast float to int 
num1 = 5.999
num1 = int(num1)
```

## dictionary <-> json
``` python
import json

dict1 = { 'name' : 'song', 'age' : 10 }
# CONVERT dictionary to json using json.dump
json_val = json.dumps(dict1)
dict2 = json.loads(json_val)
```


