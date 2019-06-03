#### 基本命令
删除镜像, container
docker rmi
docker rm

查询所有容器的id
docker container ls -aq

查询并删除所有已经退出的容器
docker rm -v $(docker container ls -f 'status=exited' -q)
docker container ls -a | awk {'print$1'}



#### dockerfile
FROM  scratch       # 制作base image
FROM  centos        # 使用官方的 base image 

LABEL  标签, 作者标签, 描述, 版本

RUN    
    eg: RUN apt-get update && apt-get install -y perl \
        pwgen --no-install-recommends && rm -rf \
        /var/lib/apt/lists/*

WORKDIR (相当于RUN cd  但不推荐使用RUN cd)   当前工作路径, 如果没有自动给创建目录
    eg: WORKDIR /test
        WORKDIR demo
        RUN pwd         # 输出结果 /test/demo

ADD and COPY
    ADD hello /    将hello 可执行文件添加到imgae 根目录
    ADD test.tar.gz /     添加到根目录并解压

    WORKDIR /root
    ADD hello test/     # /root/test/hello


ENV    # 设置环境变量, 常量


#### 容器内存限额
-m 或者 --memory: 设置内存的使用限额
--memory-swap: 



#### 容器底层技术
 - cgroup 设置进程使用CPU, 内存和IO资源的限额
 - namespace 管理host中的全局资源, 实现了容器间资源的隔离
   - Mount namespace 让容器看上去拥有整个文件系统  容器有自己的/ 根目录
   - UTS namespace   让容器有自己的hostname   默认是短ID
   - IPC namespace   拥有自己的共享内存和信号量, 实现进程间通信
   - PID namespace   容器拥有自己的一套PID
   - Network         独立的网卡,ip,路由
   - User            容器可以自己管理自己的用户, host无法看到容器中创建的用户


#### 容器网络通信
- none 除了local 没有其他任何网卡,  应用场景. 对安全性要求高并且不需要联网的应用 如 密码随机生成器 避免网络窃取
- host 连接host网络, 共享Docker host 的网络栈, 直接只用host网络最大的好处就是性能, 但是要避免端口冲突
- bridge 