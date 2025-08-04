

Installation of Jenkins:

sudo apt update 
sudo apt install openjdk-21-jdk -y

--Download the repo key
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

--create repo file
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
sudo apt-get install jenkins -y

2. Launch an Ec2 instance with Ubuntu
--checking jenkins server --systemctl status jenkins
--jenkins home directory -- ls /var/lib/jenkins (everything jenkins needs or creates will be there
except the logs file)
--Initial password --cat /var/lib/jenkins/secrets/initialAdminPassword
--Two things in Jenkins 
   1. freestyle jobs.
   2. Pipeline as a code.

3. Installing : apt install openjdk-17-jdk -y
   Path:   ls /usr/lib/jvm
   copy this in Java home : /usr/lib/jvm/java-17-openjdk-amd64 (in jenkins tools frontend)
   For above one we have installed openjdk-17 in our instance and then mentioned the path in jenkins
   frontend

  4. cat /proc/cpuinfo > cpuinfo.txt (copying the result in jenkins workspace) 

  5. in first build job (we have clone the source code , check out the source code ..build it with maven)
   **/*.war -> this means go recursively and find the war file and archive it.
   we generally save our vprofile.war file in nexus repo.

   Task 👍:
       Install jdk 11
       add that jdk11 path in jenkins
       run that and make it successfull.

       --sol add the path in Jenkins; /usr/lib/jvm/java-11-openjdk-amd64
       --will have to start from 159th lecture.

  












