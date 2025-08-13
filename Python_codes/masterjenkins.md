

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
      
   6. now will see versioning of the artifact:
     mkdir -p versions
     cp target/vprofile-2.war versions/vpro$BUILD_ID.war
     if we want which version it is then we have to check parametized and select string parameter
     cp target/vprofile-2.war versions/vpro$VERSION.war
     1. now will get the option build with parameter
        here we can provide semantic version 2.3.6 and it will be like that vpro2.3.6.war
     2. now we are enabling the time stamp with our for that we have to install build time stamp
        plugin from jenkins plugin. after doing that we have to manage jenkins and there we have to select time pattern. ddmmyy_HHmm. (cp target/vprofile-v2.war versions/vpro$BUILD_TIMESTAMP.war)
        uncheck the parametrized.
     3. now next step would be to push this artifact in s3 bucket or Nexus that will do later.

   7. if we face any disk space issue go to the instance and there in storage section increase the size and check with df -h 



-----Pipeline 👍

pipeline {
    agent any
    tools {
        maven "MAVEN3.9"
        jdk "JDK17"
    }


    environment {
        registryCredential = 'ecr:us-east-2:awscreds'
        appRegistry = "322703425874.dkr.ecr.us-east-1.amazonaws.com/vprofileappimg"
        vprofileRegistry = "https://322703425874.dkr.ecr.us-east-1.amazonaws.com"
        cluster = "vprofiles"
        service = "vprofileappsvc"
    }
  stages {
   
        stage('Fetch code') {
            steps {
               git branch: 'docker', url: 'https://github.com/hkhcoder/vprofile-project.git'
            }

        }

//    Archives the built .war artifact for later stages or audit purposes.

        stage('Build'){
            steps{
               sh 'mvn install -DskipTests'
            }

            post {
               success {
                  echo 'Now Archiving it...'
                  archiveArtifacts artifacts: '**/target/*.war'
               }
            }
        }

        // Runs unit tests using Maven.

        // Useful for validating core logic before further analysis.

        stage('UNIT TEST') {
            steps{
                sh 'mvn test'
            }
        }

        // Runs Checkstyle to analyze Java code formatting, naming, and style violations.

        // Generates a report (checkstyle-result.xml).

        stage('Checkstyle Analysis') {
            steps{
                sh 'mvn checkstyle:checkstyle'
            }
        }

// Runs sonar-scanner with:

// projectKey, projectName, projectVersion

// Paths for source code, binaries, unit test reports, coverage (jacoco), and Checkstyle results.

// This helps in identifying bugs, vulnerabilities, and code smells.

        stage("Sonar Code Analysis") {
            environment {
                scannerHome = tool 'sonar6.2'
            }
            steps {
              withSonarQubeEnv('sonarserver') {
                sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=vprofile \
                   -Dsonar.projectName=vprofile \
                   -Dsonar.projectVersion=1.0 \
                   -Dsonar.sources=src/ \
                   -Dsonar.java.binaries=target/test-classes/com/visualpathit/account/controllerTest/ \
                   -Dsonar.junit.reportsPath=target/surefire-reports/ \
                   -Dsonar.jacoco.reportsPath=target/jacoco.exec \
                   -Dsonar.java.checkstyle.reportPaths=target/checkstyle-result.xml'''
              }
            }
        }

        // Jenkins waits for SonarQube to return a Quality Gate result (pass/fail).

        // If it fails (e.g., too many issues or low coverage), the pipeline stops immediately.

        stage("Quality Gate") {
            steps {
              timeout(time: 1, unit: 'HOURS') {
                waitForQualityGate abortPipeline: true
              }
            }
          }

        stage('Build App Image') {
          steps {
       
            script {
                dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", "./Docker-files/app/multistage/")
                }
          }
    
        }

        stage('Upload App Image') {
          steps{
            script {
              docker.withRegistry( vprofileRegistry, registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
        }

        stage('Remove Container Images'){
            steps{
                sh 'docker rmi -f $(docker images -a -q)'
            }
        }


        stage('Deploy to ecs') {
          steps {
            withAWS(credentials: 'awscreds', region: 'us-east-2') {
            sh 'aws ecs update-service --cluster ${cluster} --service ${service} --force-new-deployment'
               }
          }
        }

  }
}

7. Steps:

   1. Jenkins Setup
   2. Nexus Setup
   3. Sonarqube Setup
   4. Security Group
   5. Plugins
   6. Integrate
     . Nexus
     . Sonarqube
   7. write pipeline script
   8. set Notification

   8. Now we have to Launch Nexus server
      os: Amazon Linuz 2023 AMI
      Mostly nexus and Sonar qube will be down because of budget issue
      security Group: 22 from my IP
                      8081(nexus frontend port) from my IP
                      8081 from jenkins security group(because we will be uploading our artifact from jenkins so jenkins needs to connect)
                      ls /opt/nexus
                      ec2-user@ip_address
                      take public ip:8081 and run on browser

     ----copy nexus file from hkh code to instance of nexus


     9. Sonar-Server:
        ubuntu
        22 from my ip
        80 from my IP
        80 from jenkins-sg 
        allow sonarqube-sg in jenkins on port 8080
       


    10. Plugins to install in jenkins
        Nexus
        Sonarqube
        Git
        Pipeline maven Integration Plugin
        BuildTimeStamp
        

     11. install sonar scanner plugin in jenkins
         install the sonar server details in jenkins
         add secret token from sonar to jenkins
         in sonar server security group allow traffic from jenkins server
         added private ip of sonarserver to jenkins..coz jenkins,sonar and Nexus
         are in the same vpc(virtual private cloud)
         
      12. Now we have to set the nexus repo coz once build is 
          done we need to put our artifact in nexus repo.
          1. For that we have to configure credentials for
          Nexus in Jenkin and there we have to provide username 
          and password for nexus repo.

      

          


      


                              



   
  












