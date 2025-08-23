
1. Command to set credentials for Postgress or running
docker run -d \
  --name my-postgres \
  -e POSTGRES_HOST_AUTH_METHOD=trust \
  -p 5432:5432 \
  postgres:9.6


2. docker pull redis
 
 this command is to pull the latest redis image from docker hub.
 this is simply image and for running the container u need to actually
 run it.


3. docker run redis(running the redis image in container)
runs the container in the frontend..so u have to open new terminal
and check with docker ps to check running container


4. For running the container in background (this we call as running container in detach mode)
docker run -d redis

5. For stopping container (if u got to know container crashed)
docker stop <container_id>

6. For Starting container
docker start <container_id>

7. For checking history of containers
docker ps -a

8. Now if we need to different version of redis for two different application
docker run redis:4.0 (this will pull the image and run the container)

9. Port Binding for our Laptop's port to container's port
 docker run -p6000:6379 redis
 we are doing this because our both redis container where using
 same port 6379 ..that means they were listening to the same port
 so we have make changes to avoid conflict!!

 10. Running in Detach Mode
 docker run -d  -p6000:6379 redis
 docker run -d  -p6001:6379 redis:4.0
 two differnet container on different port
 

 11. checking docker logs
 docker logs <container_id> or name
 naming the container: docker run -d -p6001:6379 --name docker-old redis:4.0

 12. For Debugging
 docker exec -it 1511ba6bc953 /bin/bash

 ===========
 root@ip-172-31-24-102:~# docker exec -it 1511ba6bc953 /bin/bash
root@1511ba6bc953:/data# ls
root@1511ba6bc953:/data# pwd
/data
root@1511ba6bc953:/data# cd /
root@1511ba6bc953:/# ls
bin  boot  data  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@1511ba6bc953:/# env
HOSTNAME=1511ba6bc953
REDIS_DOWNLOAD_SHA=1e1e18420a86cfb285933123b04a82e1ebda20bfb0a289472745a087587e93a7
PWD=/
HOME=/root
REDIS_VERSION=4.0.14
GOSU_VERSION=1.12
TERM=xterm
REDIS_DOWNLOAD_URL=http://download.redis.io/releases/redis-4.0.14.tar.gz
SHLVL=1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_=/usr/bin/env
OLDPWD=/data
================

> Docker run is to create a new container on the other hand docker start is to restart the stopped container

13. Demo Project
--have java script application,node js backend and we will be pulling
mongo image from docker hub-> docker pull mongo
then docker pull mongo-express:latest

now will do the networking between mongodb and mongo-express
docker network ls
docker network create mongo-network


----To run mongo db container
docker run -d \
> -p 27017:27017 \
> -e MONGO_INITDB_ROOT_USERNAME=admin \
> -e MONGO_INITDB_ROOT_PASSWORD=password \
> --name mongodb \
> --net mongo-network \
> mongo


--To run mongo express container and connecting  to mongodb container

root@ip-172-31-24-102:~# docker run -d \
> -p 8081:8081 \
> -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
> -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
> --net mongo-network \
> --name mongo-express \
> -e ME_CONFIG_MONGODB_SERVER=mongodb \
>mongo-express

docker logs mongo-express


Now you can login using <public_ip >8081 and make sure u have
taken care for security group for port 8081 and give username as admin
and apssword as pass

**************************************************************************************
Docker from Udemy:    
1. FOr running container in interactive mode is: docker run -it node


















