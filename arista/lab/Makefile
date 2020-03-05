REGISTRY := docker-registry
IMAGE := ceosimage
VERSION := $(shell cat ./VERSION)

.PHONY: import
import:
	docker import cEOS-lab-$(VERSION).tar $(IMAGE):$(VERSION)

.PHONY: tag
tag:
	docker tag $(IMAGE):$(VERSION) $(REGISTRY)/$(IMAGE):$(VERSION)

.PHONY: push
push:
	docker push $(REGISTRY)/$(IMAGE):$(VERSION)

.PHONY: image
image: import tag push

.PHONY: prepare
prepare:
	# create docker instances with needed environment variables
	docker create --name=ceos1 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t $(IMAGE):$(VERSION) /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker
	docker create --name=ceos2 --privileged -e INTFTYPE=eth -e ETBA=1 -e SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 -e CEOS=1 -e EOS_PLATFORM=ceoslab -e container=docker -i -t $(IMAGE):$(VERSION) /sbin/init systemd.setenv=INTFTYPE=eth systemd.setenv=ETBA=1 systemd.setenv=SKIP_ZEROTOUCH_BARRIER_IN_SYSDBINIT=1 systemd.setenv=CEOS=1 systemd.setenv=EOS_PLATFORM=ceoslab systemd.setenv=container=docker
	# create docker networks
	docker network create net1
	docker network create net2
	# connect docker instances to the networks
	docker network connect net1 ceos1
	docker network connect net1 ceos2
	docker network connect net2 ceos1
	docker network connect net2 ceos2

.PHONY: start
start:
	# start the instances
	docker start ceos1
	docker start ceos2

.PHONY: stop
stop:
	docker stop ceos1
	docker stop ceos2

.PHONY: down
down:
	# disconnect docker instances to the networks
	docker network disconnect net1 ceos1
	docker network disconnect net1 ceos2
	docker network disconnect net2 ceos1
	docker network disconnect net2 ceos2
	# remove docker networks
	docker network rm net1
	docker network rm net2
	# Remove container instances
	docker rm ceos1
	docker rm ceos2


.PHONY: shell
shell:
	docker exec -it ceos1 Cli
