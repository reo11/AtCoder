ATCODER_IMAGE := atcoder:latest
TEST_IMAGE := actoder-test:latest

default: run-atcoder

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

run-atcoder: build-atcoder
	mkdir -p ${PWD}/.tmp/online-judge-tools && \
	mkdir -p ${PWD}/.tmp/cargo-compete && \
	docker run -t -d --rm \
		-v ${PWD}:/work \
		-v ${PWD}/.tmp/online-judge-tools:/home/$(shell whoami)/.local/share/online-judge-tools/ \
		-v ${PWD}/.tmp/cargo-compete:/home/$(shell whoami)/.local/share/cargo-compete/ \
		-e "BROWSER=chrome" --name atcoder-container $(ATCODER_IMAGE) bash

exec-atcoder:
	docker exec -it atcoder-container bash

