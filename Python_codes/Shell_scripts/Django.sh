#!/bin/bash

<< COMMENT
Deploying Django Application and
Handling Errors in Shell Scripts
COMMENT

code_clone(){
    echo "cloning Dnago app.."
    git clone https://github.com/LondheShubham153/django-notes-app.git
}

install_requirements(){
    echo "Installing requirements..."
    sudo apt-get install docker.io nginx -y
}

required_restarts() {
    
    echo "Restarting services..."
    sudo chown $USER /var/run/docker.sock
    sudo systemctl enable docker
    sudo systemctl enable nginx
    sudo systemctl restart docker
}

deploy(){
    docker build -t notes-app .
    docker run -d -p 8000:8000 notes-app:latest
}


echo "******* Starting Deployment *******"

if !code_clone; then
    echo "The code is exited because the repository already exist "
    cd django-notes-app
fi

if !install_requirements; then
    echo "The code is exited because the installation failed "
    exit 1
fi

if !required_restarts; then
    echo "The code is exited because the service restart failed "
    exit 1
fi

if !deploy; then
    echo "Deployment failed, mailng the admin "
    #Sendmail
    exit 1
fi

echo "******* Deployment Completed *******"

