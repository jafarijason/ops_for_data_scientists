# [Why is Docker so Popular](https://www.section.io/engineering-education/why-is-docker-so-popular/#:~:text=Docker%20allows%20you%20to%20break,app%20and%20a%20database%20together.)

## [History of docker](https://www.slideshare.net/Docker/introduction-to-docker-2017)


## [Docker Usecases](https://medium.com/@BeNitinAgarwal/docker-usecases-3b62f4d68bc4)

## [Docker Architecture](https://www.aquasec.com/cloud-native-academy/docker-container/docker-architecture/)

## [Docker Architecture](https://docs.docker.com/get-started/overview/#docker-architecture)


## [Docker Images && Containers](https://docs.docker.com/storage/storagedriver/)

## [Lifecycle of Docker Container](https://medium.com/@BeNitinAgarwal/lifecycle-of-docker-container-d2da9f85959)

```
docker

docker pull busybox
docker pull busybox:latest

docker images
docker images | grep 'busy'

docker run busybox:latest

docker ps
docker ps -a

docker run busybox:latest echo Hello World

docker run busybox:latest ls -lah

docker rm <CI or name>

docker pull ubuntu:latest

docker images | grep 'ubuntu'

docker run -it ubuntu /bin/bash

cat /proc/cpuinfo  | grep "core"

cat /etc/os-release

docker start <container name or id>
docker ps
docker stop <container name or id>
docker rm <CI or name>


# de attach mode

docker run -it -d ubuntu:latest /bin/bash

# port forwarding
docker run -it -d -p 1234:1234 python:latest python -m http.server 1234
```

```
# Access shell to running container
docker run -it -d  --name test1 -p 1234:1234  python:latest python -m http.server 1234
docker exec -it test1

touch /home/test.txt
mkdir -p /home/testDir

exit

docker stop test1
```



