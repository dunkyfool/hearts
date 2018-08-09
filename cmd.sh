#!/bin/bash

export CURRENTPATH=`pwd`
export FOLDER=`pwd | rev | cut -d'/' -f1 | rev`

if [ "$1" = "" ]; then
	echo "./cmd.sh up|down|restart"
elif [ "$1" = "up" ]; then
	docker-compose up -d
        docker-compose exec shell jupyter notebook list | cut -d'=' -f2 | cut -d' ' -f1 | grep -v Current > token
	docker-compose exec -d shell tensorboard --logdir "/notebooks/${FOLDER}/Graph"
elif [ "$1" = "down" ]; then
	docker-compose kill
	docker-compose rm -f
elif [ "$1" = "restart" ]; then
	docker-compose kill
	docker-compose rm -f
	docker-compose up -d
        docker-compose exec shell jupyter notebook list | cut -d'=' -f2 | cut -d' ' -f1 | grep -v Current > token
	docker-compose exec -d shell tensorboard --logdir "/notebooks/${FOLDER}/Graph"
elif [ "$1" = "exec" ]; then
	docker-compose exec shell bash
else
    docker-compose ${1}
fi
