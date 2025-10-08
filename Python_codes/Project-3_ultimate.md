
1. Install docker:

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl status docker

sudo docker run hello-world

2. For adding the the group:
 <sudo usermod -aG docker ubuntu>

 3. install kubectl
 <curl -LO "https://dl.k8s.io/release/v1.31.1/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/v1.31.1/bin/linux/amd64/kubectl.sha256"
>

<echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
>

--for installing in our machine
<sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl>

---kubectl version
<kubectl version --client>
<kubectl version>
--> when you run kubectl version u will get server version and client version and at that time when someone ask kubernetes version then tell server version and when specifically ask what is what is kubectl version then tell client version.

3. Terraform installation:

<Intsall from Hashicorp>

4. <lsblk>-> for checking partion
--For resizing file system:

<sudo apt install cloud-guest-utils>
<sudo growpart /dev/xvda1>
<sudo resize2fs /dev/xvda1>

--start from 27th lecture.

<./gradlew installDist --no-daemon -Dorg.gradle.java.home=/usr/lib/jvm/java-21-openjdk-amd64
>

4. 
Vpc modules:


private subnet-> Nat gateway
public subnet -> IGW
Route table-> to connect private subnet and Nat gateway | to connect public subnet and IGW

--vpc Resources
so we will be creating Terraform resource for:
1. private subnet
2. Nat gateway
3. public subnet
4. Internet Gateway
5. Route Table



5. 

EKS modules:

iam roles -> cluster(Master Plane) -> policy
iam roles -> node(Data Plane) -> policy

Resources:

1. iam role cluster
2. policy
3. eks cluster

4. iam role node
5. policy
6. Node Group--> attach this to  EKS cluster











