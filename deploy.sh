#!/usr/bin/env bash

function finish() {
        echo "Exiting"
	docker-compose -f docker-compose.yml down
}

trap finish SIGINT

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d db1
docker-compose -f docker-compose.yml up -d db2
sleep 3
docker-compose -f docker-compose.yml up -d web
docker-compose -f docker-compose.yml up nginx
