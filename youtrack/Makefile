COMPOSE_FILE=docker-compose.yml
all: uplog

update: stop clean build uplog
up: acme uplog

# up and show logs
build:
	docker-compose -f $(COMPOSE_FILE) build --pull --no-cache

clean:
	docker-compose -f $(COMPOSE_FILE) down --rmi all

stop:
	docker-compose -f $(COMPOSE_FILE) stop

uplog:
	docker-compose -f $(COMPOSE_FILE) up -d && docker-compose -f $(COMPOSE_FILE) logs -f -t --tail=10

