
1. AWS LIFT AND SHIFT



--app server(tomcat that runs on 8080), backend server(rabbit mq, memcached, db01), ELB(for having connected to app so that ELB will be providing IP adress)

-- First thing we have to create the security group for ELB, backend and for app server

--for the app server security group we have to give all the acceess that is allowing from ELB in inbound rule, also giving access to 22 so that we can ssh into it.

--create security group for ELB and in this allow access to HTTPS and HTTP for IPV4 and IPV6.

--now, for creating the security group for backend server we have to allow in inbound rule that is coming from app server!. and we have to also give access to all internal 
  traffic between MYSQL-3306, Memcached-5672, rmq-1121. so that they can interact with each other!
  
--once it is done we have create the EC2 instances for app server,memcached(mc01),rabbitmq(rmq01), db01..and in that app server we have to put the security group for app server,
and for the rest three that is the backend we have to give the sceurity group for backend.

--Now we have to create Route 53 to map the servers name that is there in configuration file that is in  db ,memcached,rabbitmq. we have created the hosted zone with the name 
vprofile.in
 and inside that we have created the records for app,db,mq,mc and in configuration of this we have put the subdomain name such app01 that will come as app01.vprofile.in and 
  parallel to record type we have to put A that name to Ip matching and in the value section we have to put private IP address of those three servers and the same name that we 
  getting here we have replace that in configuration file.

--For checking whether the we are reciveing the packets from the app server to these backend servers , we have to take the public IP address from the app servers ec2 instances
  and ssh into it. and run this command to check whether we are receiving the packets or not ---- ping -c 4 mc01.vprofile.in --- replace it with rmq01,app01,db01.

--Now we have to create the s3 bucket for putting the war file that we are going create locally with the command mvn install. so we created the s3 bucket and make sure the bucket
  name is unique. after creating the s3 with we have to create IAM role and put that IAM role in app server instance. 

--Now we have to go back to the visual studio where our code is available and there we have to run mvn install that will create the vprofile.war file in target folder. we have to
  do aws configure and provide aaccess keys and then do ls target/ there u will see war file. Now we have to run the command 
  aws s3 cp target/vprofile-v2.war  s3://vprofile-las-artifact5/ to copy the file from your current location to s3 bucket. Do this to list aws s3 ls s3://vprofile-las-artifact5/
  
--Now we have to login to app server with public ip address and ssh . we are doing that because we want to copy the that war file from s3 bucket to that app server
  >> After login we have to install aws cli in that server with this command snap install aws-cli --classic
  >> Now for copying the file from s3 to app server. we have to do this aws s3 cp s3://vprofile-las-artifact5/vprofile-v2.war /tmp/
  >> Now once its done we have to stop that tomcat10 server that is running with the command systemctl stop tomcat10
  >> once the server stopped we have to remove the file that is there in tomcat path. rm -rf /var/lib/tomcat10/webapps/ROOT
  >> once its  remove check ls /var/lib/tomcat10/webapps/ROOT
  >> Now copy the file that is there in tmp on your app server to that tomcat path location.  cp /tmp/vprofile-v2.war /var/lib/tomcat10/webapps/ROOT.war
  >> once its done start the tomcat server with systemctl start tomcat10.
  >> now u can check in the path you will see root and root.war file . ls /var/lib/tomcat10/webapps/
  
  
 -- we can use the vprofile ip address (public one) but before that to access the application in app server we have to give inbound rule access of port 8080 from my IP.
    Now we can access the Ip address from app server but we want to access that via load balancer.
 -- we have to create the target group and add that app01 in that.After creating the target we have to create the load balancer.
 -- once Load balancer created add the security group of Load balancer that we have created earlier.
 --Now you will get the link in the load balancer and u can access the website from there
 --if you want to HTTPS connection then you have to take that link and add that in Go Daddy.
 
 
 --Now will do auto scaling.for that we have to cretae image in appserver and Launch template as well. These two things would be required while creating austoscaling group
   and then we have to create the austoscaling group and we are creating the autoscaling to scale in and scale out the the instance in different scenarios such as cpu
   utilization and all. and in autoscaling group we have one instance name vprofile-app that is going to manage autoscaling and at that time we can delete vprofile-app01 if
   we want. we have done infrastucture as a service(means instances). we shifted our application from local to aws.
   

   

  
  