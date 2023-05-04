ATCODER_IMAGE := atcoder:latest
ATCODER_CONTAINER_NAME := atcoder-container
TEST_IMAGE := actoder-test:latest

default: run-atcoder
run: run-atcoder
build: build-atcoder
stop: stop-atcoder

build-test:
	docker build --build-arg UID=$(shell id -u) --build-arg UNAME=$(shell whoami) -t $(TEST_IMAGE) -f dockerfiles/Dockerfile.test .

run-test: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pytest test/*

lint: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen run lint

auto-lint: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen run format

run-lint-generate: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen generate .

build-atcoder:
	docker build --build-arg UID=$(shell id -u) --build-arg UNAME=$(shell whoami) -t $(ATCODER_IMAGE) -f dockerfiles/Dockerfile .

ifeq ($(shell docker ps -a --format '{{.Names}}'| grep $(ATCODER_CONTAINER_NAME)),)
run-atcoder: build-atcoder
	mkdir -p ${PWD}/.tmp/online-judge-tools && \
	mkdir -p ${PWD}/.tmp/cargo-compete && \
	docker run -t -d --rm \
		-v ${PWD}:/work \
		-v ${PWD}/.tmp/online-judge-tools:/home/$(shell whoami)/.local/share/online-judge-tools/ \
		-v ${PWD}/.tmp/cargo-compete:/home/$(shell whoami)/.local/share/cargo-compete/ \
		-e "BROWSER=chrome" --name $(ATCODER_CONTAINER_NAME) $(ATCODER_IMAGE) bash && \
	clear && \
	docker exec -it $(ATCODER_CONTAINER_NAME) bash
else
run-atcoder:
	clear && \
	docker exec -it $(ATCODER_CONTAINER_NAME) bash
endif

stop-atcoder:
	docker stop $(ATCODER_CONTAINER_NAME)
