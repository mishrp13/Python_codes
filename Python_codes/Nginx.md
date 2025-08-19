

1. scp -i ~/Downloads/vprobeankey.pem -r /c/Nginx_crash_course/ ubuntu@54.242.123.21:/home/ubuntu
--make sure to remove node modules from your local and then copy to ec2 instance and there run npm install

docker build -t myapp:1.0 .

docker run -p 3000:3000 myapp:1.0

docker-compose up --build -d

Notes:

1. created Ngnix folder
wrote server.js,wrote some dependencies in packag.json,docker compose file,docker file,index.html

2. created EC2 instances
there copied all the content from Ngnix folder to ec2 instance with scp command and made sure that opening three different ports in security group.

3. Putting the right folders and files at right places
once we are inside ec2 make sure that have your docker file and docker compose file inside the Ngnix folder and ur index.html file inside public or you can put index.html file directly inside Ngnix folder but make the changes in docker file accordingly!!


4. Run the Docker compose file
As we have created simple docker file where we have mentioned for 1 app and then creted docker compose file and took the help of docker file to create 3 servers or 3 apps!!





![alt text](image-1.png)


