pg_con:
	run -it --name pg -e POSTGRES_PASSWORD=1 -p 5433:5432 -d postgres:alpine

build:
	docker build -t restobot:alpine .
	docker run -it --name resto_bot_con restobot:alpine


restart:
	docker container stop resto_bot_con
	docker container rm resto_bot_con
	docker image rm resto:alpine
	docker build -t resto:alpine .
	docker run -it --name resto_bot_con restobot:alpine




