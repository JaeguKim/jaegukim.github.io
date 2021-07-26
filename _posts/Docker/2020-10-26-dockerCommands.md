---
layout: post
title:  "[Docker] 자주 사용하는 커멘드"
date:   2020-10-26
categories: [Docker]
---
```docker-compose up```
-Builds, (re)creates, starts, and attaches to containers for a service
(```-d, --detach``` : Detached Mode, Run container in background.)   

```docker rmi <your-image-id>``` : delete image with id   

```docker images``` : list docker images   

```docker build --tag <tag-name> . ``` : build docker image in current directory with tag name   

```docker tag bb38976d03cf yourhubusername/verse_gapminder:firsttry``` : tag already created image  

```docker push yourhubusername/verse_gapminder``` : push image to docker hub repo

| 동작 | 커멘드 
| -- | --
| 현재실행중인 컨테이너 정보 | ```docker container ls```
| running or stopped 컨테이너 정보 | ```docker container ls -a```
| 컨테이너 삭제 | ``` docker container rm (-f) [CONTAINER ID]```
| 컨테이너 실행 | (예시) ``` docker container run --publish 3306:3306 -d --name mysql -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql ```
| 한 컨테이너 내의 프로세스 리스트 | ```docker container top [CONTAINER NAME]```
| 한 컨테이너 내의 config 세부정보 | ```docker container inspect [CONTAINER NAME]```
| 모든 컨테이너들에 대한 performance stat | ```docker container stats [CONTAINER NAME]```
| 새로운 컨테이너를 interactive하게 start | ```docker container run -it [CONTAINER NAME] ```
| 기존의 컨테이너에게 추가적인 커멘드 실행 | ```  docker container exec -it -run [ADDITIONAL COMMAND] ```
| 다른 Dockerfile을 명시하여 build | ``` docker build -f some-dockerfile ```
| 현재경로를 컨테이너 내에 /site경로로 마운트 | ``` docker run -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve ```
| 이미지 빌드시 ARG 전달 하는 예시 | ``` docker build --build-arg base_img=spark_img .```