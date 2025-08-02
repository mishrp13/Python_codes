

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





