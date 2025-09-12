
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
18. Replica set helps in creting replicas of pods
19. Staeful sets gives numbering to pods
20. Deployment will also create replica set but it will also helps in rolling updates.
21. <kubectl delete -f pod.yml> we are doing this because our deployment.yml is going to create pod
22. <kubectl apply -f deployment.yml>

23. <kubectl get deployment -n nginx>

24. <kubectl scale deployment/nginx-deployment -n nginx --replicas=5> it will scale up pods to 5.

25. <kubectl set image deployment/nginx-deployment -n nginx nginx=nginx:1.27.3> kind of rooling update

26. <kubectl get pods -n nginx -o wide>
--start from 2 hours 8 minutes