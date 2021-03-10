---
layout: post
title: "Web Dev Commands"
date: 2020-11-01 18:59:00 +0900
categories: [Shortcut]
---
- Show console/Close inspect window  
`Cmd + Option + J`

- Show element  
`Cmd + Option + C`

- Kill process concerned with port 8000  
`sudo lsof -t -i tcp:8000 | xargs kill -9`
 
- Exporting Spring Boot application to jar file with maven  
` ./mvnw clean package` 

- Exporting Spring Boot application to jar file without testing  
`./mvnw clean package -DskipTests`

