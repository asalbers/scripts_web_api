#!/bin/sh
echo "name of container (web_api-BLUE)\n "
read -r container_name
echo "image name: (web_api:blue):\\n"
read -r image_name

if [ $container_name == "web_api-BLUE" ]
then
docker run --name=$container_name --net=web -d $image_name
fi
if [ $container_name == "web_api-GREEN" ]
then
docker run --name=$container_name --net=web  -d $image_name
fi