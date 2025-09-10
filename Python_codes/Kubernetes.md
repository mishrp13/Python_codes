
1. sudo usermod -aG docker $USER && newgrp docker
2. Install kind,kubectl,docker from shubham's repo.
3. <kind create cluster --name=tws-cluster --config=config.yml>
4. <kubectl get nodes>
5. <kubectl get nodes --context kind-tws-cluster>
6. <minikube delete>
7. <kubectl config use-context kind-tws-cluster> for switching the cluster
8. <kubectl get namespace>
9. <kubectl get pods -n kube-system>
10. <kubectl create ns nginx>
11. namespace->pod->deployement->service->user
12. <kubectl run nginx --image=nginx>
13. <kubectl delete pod nginx>
14. <kubectl run nginx --image=nginx -n nginx>
15. <kubectl apply -f namespace.yml>
16. <kubectl apply -f pod.yml>
17. <kubectl exec -it nginx-pod -n  nginx -- bash>
start from 1 hour 45 minutes