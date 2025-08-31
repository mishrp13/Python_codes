
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
1. For running container in interactive mode is: docker run -it node

---As we are coping the node app starting foder from local to ec2 instance
scp -i ~/Downloads/vprobeankey.pem -r ~/downloads/assignment-problem/ ubuntu@54.167.39.132:/home/ubuntu

---> TO create an image based on our docker file: docker build . and after that you write docker run -d -p 3000:80 <container_id>

--->whenever we are making changes in the code and thinking when we restart our container then it will automatically staring reflecting in the client side so the answer is no instead we have to build the image again and then run re-start the container and then changes will start reflecting in client side!


2. It's not always necessary to to run docker run to start a container whenever we do that , that means we are starting a new container so sometimes it required but not always so..at some point we need to run stopped to containers at that time we have to check stopped containers with the command <docker ps -a> and then run <docker start> and you will see that container will be up and running!!

3. Attached means when we want to run containers and see the ouput continously in the console and the command we can write <docker run -p 3000:80 <image_id> > . In this case it will run in attached mode by default instead if we run the same container in detached mode then <docker run -p 3000:80 -d <image_id>>. if the container is already there and we need to start the stopped container then <docker start <container_id>> and here the container will be running in detached mode by default. if we want to make the running container in attached mode then <docker attacher container_id>. or if you directly want to start the container in attached mode then simply <docker start -a <container_id>>. If you simply want to check the logs then<docker logs <container_id>> or you want continous output in your console then <docker logs -f <container_id>>.

4.(FROM python

WORKDIR /app

COPY . /app 

CMD ["python", "rng.py"])

---> <docker run -it <container_id>> to run in interactive mode
---> <docker start -a -i <container_id>> interactive mode!!

5. For removing containers and images:
<docker stop <container_id>>
<docker rm <container_id>>
<docker container prune>--> to remove all conatiner in one go
<docker rmi <image_id>>
we can't directly remove image first instead we need to remove the running and stopped containers first!!

6. To remove the container directly whenver we stop it:
<docker run -p 3000:80 -d --rm <container_id>>
here if we do <docker stop <container_id>>
container will remove automatically after stopping it!!

7.For checking Docker images
<docker image inspect <image_id>>--> you will get to see layers
--start from lec36


8. if we want to name our container:

<docker run -p 3000:80 -d --rm --name golgappa <container_id>>

9. For using name:tag while building the image

<docker build -t goals:latest .>
then we can run <docker run -p 3000:80 -d --rm --name  goalsapp goals:latest>

10. For Removing image 👍
docker image prune -a

11. Now once the image is build we need to push it somewhere so the place is Dockerhub Repo
--> docker build -t mishrp/node-hello-world .
--->docker login
---->docker push mishrp/node-hello-world
----> or if you want to use the image that is already in your local then 
<docker tag node_demo:latest mishrp/node-hello-world .> then do the docker push!!

12. To delete all local image:<docker image prune -a>

13. Now copying file from local to ec2 to understand the concept of volumes in docker.
There are mainly two types of data i.e temporary and permanent!
scp -i ~/Downloads/vprobeankey.pem -r ~/downloads/data-volumes-01-starting-setup/ ubuntu@54.147.145.168:/home/ubuntu

14. For building the image with tag: <docker build -t feedback-node .>

15. The real problem with the containers is the storing the data inside that let's say
we created container and we are storing files in that for some users and once we stop container and deleted it then all the data will be lost because container itself got deleted on the other hand if we stop the container and then start it again the data will still be there because container never got deleted. But we won't be always working with same container instead we will be creating the container with the latest images and we don't want previous containers or we can say we will be deleting older containers but we want the data of the users. so that's the problem and we will be solving that with volumes.!

16. Unsuccessful try:
so we have added volume instruction in our dockerfile with <Volume[/app/feedback]> so that whatever we are saving in our text should get saved in /feedback/title.txt and did some modification in server.js file even after doing that file is not getting saved in feedback folder after stopping and starting new brand container. so we want our data to be saved even container gets stopped or removed and after starting new container old data should be there! will check in next lecture!

17. So there are two types of volumes one is Anonymous volume till now we were trying with anonymous volumes that's why data was not persist. Now we will be trying with named volumes and there the data will get stored in Feedback folder. The basic difference is anonymous volume we were calling via writing inside the dockerfile on the other hand name volume we are calling while running the container.
For building: <docker build -t feedback:volumes .>
For Running:<docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback feedback:volumes>

18. Bind Mount gives us two thing one is to store data and another one is write on data.In this Bind Mount we are getting access of entire folder path and mounting it with the app directory inside the docker file that we have created and if we make changes outside the docker file and inside the folder the changes will reflect without building image again beacuse the app directory in bind mount with path where the code is located.
<docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback -v "/home/ubuntu/data-volumes-01-starting-setup/data-volumes-01-starting-setup:/app" feedback:volumes
>
--> But with this when we run the container then container will crash immidiately because it won't be able to find express module. as we are having Run NPM install in docker file but this time app directory is bind mount with path where the code is located.

19. To get rid of the above issue we have have to now add anonymous volume to add node modules.
<docker run -d -p 3000:80  --name feedback-app -v feedback:/app/feedback -v "/home/ubuntu/data-volumes-01-starting-setup/data-volumes-01-starting-setup:/app" -v /app/node_modules feedback:volumes
>
--> that will all node modules that is required for this application to run and now what is happening here local folder is overriding the code that is there inside the docker file and that is why we were facing earlier because we were not having node modules in that folder and to git rid of that we are explicitly mentioning the annonymous volume to add that node modules << -v /app/node_modules >>.
--> After this we will get the application working as before and now we will be having one more benifit if we make any changes in index.html file then at that time we don't have to build docker image again instead it will automatically fetch the changes once we save the index.html file. Its happening because the our container's app directoty is mounted with local folder where the code is located!

20. Sometime if we do some consol.log("Hi") in server.js file then it will not start reflecting in logs directly so at that case we have to stop and start container and that is actually not a good startegy. Instead of that we have to wirte some dependencies in pacakage.json such as : 

< 
"scripts": {
    "start": "nodemon server.js"
   },
  "dependencies": {
    "body-parser": "^1.19.0",
    "express": "^4.17.1"
  },
  "devDependencies":{
    "nodemon":"2.0.4"
  }
>

and in Docker file:
CMD ["npm", "start"]

-->now if we do changes in server.js with console.log("Hi") it will start showing when we write docker logs<container_id>

















