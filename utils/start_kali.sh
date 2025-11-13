#!/bin/bash
set -e

CONTAINER_NAME=$1
IMAGE_NAME=$2
NETWORK_NAME=$3   
LOCAL_IP=$4


if [ "$(docker ps -a -q -f name=^/${CONTAINER_NAME}$)" ]; then
    echo "Container $CONTAINER_NAME exists"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME    
fi


docker run -d -it \
  --name $CONTAINER_NAME \
  --network $NETWORK_NAME \
  --ip $LOCAL_IP \
  $IMAGE_NAME

echo " New attack container $CONTAINER_NAME started"