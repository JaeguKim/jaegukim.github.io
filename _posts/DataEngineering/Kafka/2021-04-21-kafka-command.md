---
layout: post
title: "Kafka Command"
date: 2021-04-21 17:09:00 +0900
categories: [DataEngineering,Kafka]
---

## kafka console consumer에서 custom deserializer 설정해서 record 읽기

``` sh
bin/kafka-console-consumer.sh --topic number-of-people-by-place --bootstrap-server localhost:9092 \
 --from-beginning \
 --property print.key=true \
 --property key.separator=" : "  --key-deserializer "org.apache.kafka.common.serialization.IntegerDeserializer" \  --value-deserializer "org.apache.kafka.common.serialization.IntegerDeserializer"
 ```