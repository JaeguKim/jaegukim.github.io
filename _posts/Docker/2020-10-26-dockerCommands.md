---
layout: post
title:  "[Docker] 자주 사용하는 커멘드"
date:   2020-10-26
categories: [Docker]
---

- Builds, (re)creates, starts, and attaches to containers for a service
> docker-compose up (-d : detached mode)

- delete with id
> docker rmi [image id]

- list images
> docker images

- build image
> docker build --tag [tag-name] --build-arg [key]=[value] . 

- push image
> docker push [registry:tag]

- list running container
> docker container ls

- run container
> docker container run [-it : interactive mode] --publish [container port]:[host port] [-d] --name [name] -e [key]=[value]

- delete container
> docker container rm (-f) [CONTAINER ID]

- run container
> docker run --name [container name] [tag]
