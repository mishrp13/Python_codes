
## Flow of pipeline

1. Aws code commit -> Aws Code pipeline -> Aws Code build -> AWS code deploy

## Aws code pipleline

2. Mostly organisation uses Jenkins for continous Integration and conntinous delivery.
Steps:
1. Jenkins impliments continous Integration with its declarative code in Jenkins and things that goes into it is check out, Build & UT, code scan, Image build, Image sacan, Image push and this building images happening via Docker
2. After that Jenkins invoke continous delivery using Ansible or shell script which are outdated way or we can use platform like argo-cd which is git ops based platform (Helm charts). Git ops is the best way of implementing continous delivery
3. once the docker image is creates we can write the shell script to write a kubernetes yaml file and push file in Kubernetes cluster or we can create a helm chart using some shell script or python and again use kubectl or helm command to push it to one kuberentes cluster.if multiple Kubernetes cluster then we do that by writing ansible playbook but the recommended approach is using gitops.

4. Aws CICD:
so here we will be having Aws code commit in place of git hub then aws code pipeline and that aws code pipeline invokes AWS codeBuild and in that code scanning and building of image takes place after that same aws codepipeline invokes Aws codedeploy and there it push the code in Kubernetes cluster or AWs Elastic Container registory.