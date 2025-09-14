
1. echo "Hello" | tee hello.txt -> will print output as well put the result in hello.txt

2. diff demofile.txt  hello.txt

3. ln -s path/file -> create the soft link

4. ln path/file hardlink -> create the hardlink and it generally won't get destroyed even after original file deletion.

5. df -h, free -m -> disk space

6. nohup free -m -> it collects the record and give back in nohup.out and after that if we do nohup df -h then df -h logs will will be collected as well. so will collect records.

7. vmstat-> virtual memory


*** System Level commands ****

8. uname-> tells which platform we are using

9. uptime -> users and logged in 

10. who -> gives the list of users who logged in and at what time

11. whoami -> gives the list of current user

12. which python -> gives details where python is installed and debug it.

13. id -> details for users,group.

14. sudo shutdown

15. sudo reboot

16. sudo apt update -> updating the package

17. sudo apt-get install docker.io -> to install docker from internet

18. control+r -> for reverse search and get details and enter

19. which dokcer -> u can check where docker is installed

20. sudo apt remove docker.io

21. yum-> works on centos, apt-> works on ubuntu for package manager, dnf -> fedora, pacman -> arch linux, portage-> gentoo as Application package manager.


*** User and group Mangement ****

22. sudo useradd -m jethalal -> adding jethalal in home where ubuntu is there. check in home you will find both ubuntu and jethalal

23. sudo passwd jethalal -> changes the passwd

24. su jethalal -> switch user

25. cat /etc/passwd -> gives the details what all the users got added

26. sudo userdel jethalal

--start from 2 hour 35 min



