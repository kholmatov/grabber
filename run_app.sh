#!/bin/bash
imageName=grabber
containerName=$imageName

docker build -t $imageName -f Dockerfile  .

echo Delete old container...
docker rm -f $containerName

echo Run new container...
docker run -d -p 8000:8000 --name $containerName $imageName
docker logs -f $containerName
