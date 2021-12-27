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

## Difference between == and is operator
`==` compares the values of both the operands and checks for value equality. `is` checks if both operands refer to the same object or not.

## TypeError: sequence item 0: expected str instance, int found
`''.join(list_name)` 을 쓸때, list의 모든 element들은 문자여야한다. 즉 list에 저장된 값이 정수이거나 실수이면 에러가 발생한다.