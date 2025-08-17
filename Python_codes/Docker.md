
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

--Now have to create the database name user-account from the front end of mongo express

----------Projects 

🟢 Beginner-Level Projects

Static Website (HTML/CSS/JS)

Put a static site in an nginx container.

Push to Docker Hub as yourname/static-website.

Learn: basics of Dockerfile, ports, volumes.



----------->


---general stuff:

#!/bin/bash

# Install docker on Ubuntu
sudo apt-get update
   sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install docker-compose
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io -y
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose

# Add ubuntu user into docker group
    sudo usermod -a -G docker ubuntu


  1. scp -i your-key.pem -r static-website/ ubuntu@<EC2_PUBLIC_IP>:/home/ubuntu/

  scp -i vprobean -r STATIC-WEBSITE/ ubuntu@3.95.63.197:/home/ubuntu
  --$ scp -i ~/Downloads/vprobeankey.pem -r Static-website/ ubuntu@3.95.63.197:/home/ubuntu
 ---we are writing -r here becuase we want to copy entire folder!! otherwise it will copy only file like index.html

 cd ~/static-website
sudo docker build -t my-static-website .
sudo docker run -d -p 80:80 my-static-website






Python Flask / Node.js Express App

Build a small REST API (like /hello → returns JSON).

Dockerize it and push.

Learn: base images (python:3.11, node:18), app dependencies, port mapping.

Simple Redis-backed Counter App

Flask/Express frontend → Redis backend → count visits.

Use docker-compose to run 2 containers together.

Push your app image + practice multi-container networking.

🟡 Intermediate-Level Projects

To-Do App (Full Stack)

Backend: Flask/Node/Go.

DB: MongoDB or PostgreSQL.

Frontend: React or Angular.

Use docker-compose for 3 services (frontend, backend, DB).

URL Shortener (like Bitly)

Store short URLs in Redis/Mongo.

Backend API + simple frontend.

Add healthcheck in Dockerfile.

WordPress + MySQL

Run WordPress connected to MySQL via docker-compose.

Publish a tutorial repo + pre-configured Docker Hub image.

🔴 Advanced-Level Projects

Microservices Demo

Create 2–3 services (e.g., user-service, order-service, product-service).

Use RabbitMQ or Kafka for communication.

Deploy all via docker-compose.

CI/CD Pipeline Demo

Create a small project and build Docker image automatically with GitHub Actions.

Push image to Docker Hub on each commit.

Monitoring Stack

Spin up Prometheus + Grafana + Node Exporter with docker-compose.

Publish a tutorial like: “Monitoring your Dockerized App with Grafana”.

Custom Docker Base Image

Create your own lightweight image (e.g., alpine + Python + some pre-installed tools).

Push to Docker Hub as yourname/python-tools.

⚡ Each of these projects teaches a new Docker skill:

Building images (Dockerfile)

Running multiple containers (docker-compose)

Networking between containers

Volumes for persistence

Multi-stage builds (for smaller images)

CI/CD with GitHub + Docker Hub



 


