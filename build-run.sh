#sudo docker kill $(sudo docker ps -q)
./hooks/post_checkout


mkdir /fcUsers


sudo docker ps -q --filter ancestor="mmiscool/fc-docker" | xargs -r sudo docker stop

#sudo docker run -d  -v $(pwd):/workspace -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -p 8181:8181 sapk/cloud9 --auth username:password
#sudo docker build . -t mmiscool/fc-docker
sudo docker run -d -p 80:80 mmiscool/fc-docker

sudo docker run -d kewl


echo IP address of docker containers are
sudo docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'  $(sudo docker ps -q)
#sleep 10
#firefox $(sudo docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'  $(sudo docker ps -q)) &
cd proxyServer
./build-run.sh 
cd ..

