# shell

sudo docker stop test
sudo docker rm test
sudo docker rmi zoneslee/dockerproject:v1.0

sudo docker build -t zoneslee/dockerproject:v1.0 .

# 指定grpc的服务端口
sudo docker run --name test -p 50001:50001 -v /home/lighthouse/LogInfo/DockerPythonLog:/usr/src/app/docker_project/log zoneslee/dockerproject:v1.0
