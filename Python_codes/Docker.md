
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
 docker run -d  -p6000:6379 redis
 two differnet container on different port
 start from 57 minutes



 


