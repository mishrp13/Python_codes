
1. echo "Hello" | tee hello.txt -> will print output as well put the result in hello.txt

2. diff demofile.txt  hello.txt

3. ln -s path/file -> create the soft link

4. ln path/file hardlink -> create the hardlink and it generally won't get destroyed even after original file deletion.

5. df -h, free -m -> disk space

6. nohup free -m -> it collects the record and give back in nohup.out and after that if we do nohup df -h then df -h logs will will be collected as well. so will collect records.

7. vmstat-> virtual memory


*** System Level commands ******

8. uname-> tells which platform we are using

9. 