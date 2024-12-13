# shell

sudo docker rm test
sudo docker rmi zoneslee/dockerproject:v1.0

sudo docker build -t zoneslee/dockerproject:v1.0 .

sudo docker run --name test zoneslee/dockerproject:v1.0
