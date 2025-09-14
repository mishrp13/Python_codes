
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
--Daemon set will make sure in every worker-nodes,  pod will be running
21. <kubectl delete -f pod.yml> we are doing this because our deployment.yml is going to create pod
22. <kubectl apply -f deployment.yml>

23. <kubectl get deployment -n nginx>

24. <kubectl scale deployment/nginx-deployment -n nginx --replicas=5> it will scale up pods to 5.

25. <kubectl set image deployment/nginx-deployment -n nginx nginx=nginx:1.27.3> kind of rooling update

26. <kubectl get pods -n nginx -o wide>

27. <kubectl logs pod/demo-job-s8b86 -n nginx>

28. <apiVersion: batch/v1
kind: CronJob
metadata:
  name: minute-backup
  namespace: nginx
spec:
  schedule: "* * * * *"
  jobTemplate:
    spec:
      template:
        metadata:
          labels:
            app: minute-backup
        spec:
          containers:
          - name: backup-container
            image: busybox
            command:
            - sh
            - -c
            - >
              echo "Backup started";
              mkdir -p /backup;
              mkdir -p /demo-data &&
              cp -r /demo-data /backup &&
              echo "Backup completed";
            volumeMounts:
            - name: demo-data-volume
              mountPath: /demo-data
            - name: backup-volume
              mountPath: /backup
          restartPolicy: OnFailure
          volumes:
          - name: demo-data-volume
            hostPath:
              path: /demo-data
              type: DirectoryOrCreate
          - name: backup-volume
            hostPath:
              path: /backup
              type: DirectoryOrCreate
>

29. <kubectl logs pod/minute-backup-29294349-fvbgz -n nginx>

30. Persitentvolume: with this created volume of 1 gb from host machine
 <apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
  namespace: nginx
  labels:
    app: local
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  hostPath:
    path: /mnt/data

>

31. Persistentvolumeclaim: this is to claim the volume from persistentvolume that we created earlier! <kubectl get pv> to check how much volume is available

<apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
  namespace: nginx
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: local-storage

>

32. Now after creating the claim will give to our pod.

<apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        volumeMounts:
        - mountPath: /var/www/html
          name: my-volume
      volumes:
      - name: my-volume
        persistentVolumeClaim:
          claimName: local-pvc
>

33. (Namespace) pods(grouped)-> deployment(grouped)-> services -> user

34. service.yml file:
  <apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: nginx
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
>

35. <kubectl get pods -n nginx>
    <kubectl get all -n nginx>


36. <sudo -E kubectl port-forward service/nginx-service -n nginx 81:80 --address=0.0.0.0>

37. Namespace-> nginx container-> pod -> deployment-> service->user


----Mini project

{
38. <docker build -t notes-app-k8s .>--> first thing will create docker image

39. this image wont run locally instead we have to push it to docker hub to run it via kubernetes

40. <docker image tag notes-app-k8s:latest mishrp/notes-app-k8s:latest>
for tagging the image with dockerhub profile name so that we can push it in dockerhub so that we can later use it 

41. <docker push mishrp/notes-app-k8s> -> pushed it to docker hub

42. Kubernetes will only pull if it is publicly available, we can do privately but again we have to give it access

43. deployment.yml <apiVersion: apps/v1
kind: Deployment
metadata:
  name: notes-app-deployment
  labels:
    app: notes-app
  namespace: notes-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: notes-app
  template:
    metadata:
      labels:
        app: notes-app
    spec:
      containers:
      - name: notes-app
        image: mishrp/notes-app-k8s
        ports:
        - containerPort: 8000
>

this will take care of pods

44. namespace.yml <kind: Namespace
apiVersion: v1
metadata:
  name: notes-app
>

45. service.yml <kind: Service
apiVersion: v1
metadata:
  name: notes-app-service
spec:
  selector:
    app: notes-app
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
>

----so basically we build the image and then pushed it docker hub after that we have created namespace, then created deployment file and there we mentioned the image that we have pushed in docker and after that we have created service.yml file. now will expose that port.

46. <kubectl port-forward service/notes-app-service -n notes-app 8000:8000 --address=0.0.0.0>

}

47. Now we are going to use nginx to re-route the traffic and to do that in previous namespace will change it back to nginx

48. run this command in kuber-in-one-shot to install ingress-nginx <kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml>

49. ingress.yml
  <apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-notes-ingress
  namespace: nginx
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - pathType: Prefix
        path: /nginx
        backend:
          service:
            name: nginx-notes
            port:
              number: 80
      - pathType: Prefix
        path: /
        backend:
          service:
            name: notes-app-service
            port:
              number: 8000

>


50. our ingress controller running in port:8000
<sudo -E kubectl port-forward service/ingress-nginx-controller -n ingress-nginx 8000:80 --address=0.0.0.0>

51. For django,spring boot we generally use deployment, replicaset,deamonsets and on the other hand for mysql we use stateful sets and these are sequentially numbered even if one pod goes down and the new pod comes up then that pod will be sequentially numbered. In statefulsets we generally have our data persisted.

52. namespace <kind: Namespace
apiVersion: v1
metadata:
  name: mysql
>

53. service <apiVersion: v1
kind: Service
metadata:
  name: mysql
  namespace: mysql
spec:
  clusterIP: None
  selector:
    app: mysql
  ports:
    - protocol: TCP
      port: 3306
      targetPort: 3306>

54. statefulset:
 <apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql-statefulset
  namespace: mysql
spec:
  serviceName: mysql-service
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:   # <-- singular, not templates
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        ports:
        - containerPort: 3306
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: root
        - name: MYSQL_DATABASE
          value: devops
        volumeMounts:
        - name: mysql-data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:   # <-- moved out of template
  - metadata:
      name: mysql-data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
>

55. <kubectl exec -it mysql-statefulset-0 -n mysql -- bash>

56. <kubectl delete pod  mysql-statefulset-0 -n mysql> --> even after you delete it will get automically created with the same name becuase of it stateful set. here it's service,environment variable everything is tightly coupled and that's why it takes everything together.

--start from from 4 hour 10 min
