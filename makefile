ATCODER_IMAGE := bluexleoxgreen/atcoder:1.0.0
ATCODER_NEW_IMAGE := bluexleoxgreen/atcoder:2.0.0
ATCODER_CONTAINER_NAME := atcoder-container

default: run-atcoder
run: run-atcoder
build: build-atcoder
stop: stop-atcoder
test: run-test

# requier `docker login` before push

build-atcoder:
	docker build --build-arg UID=$(shell id -u) --build-arg UNAME=$(shell whoami) -t $(ATCODER_IMAGE) -f dockerfiles/Dockerfile .
	docker push $(ATCODER_IMAGE)

build-new-image:
	docker build --build-arg UID=$(shell id -u) --build-arg UNAME=$(shell whoami) -t $(ATCODER_NEW_IMAGE) -f dockerfiles/Dockerfile.new .
	docker push $(ATCODER_NEW_IMAGE)

ifeq ($(shell docker ps -a --format '{{.Names}}'| grep $(ATCODER_CONTAINER_NAME)),)
run-atcoder:
	mkdir -p ${PWD}/.tmp/online-judge-tools && \
	mkdir -p ${PWD}/.tmp/cargo-compete && \
	docker run -t -d --rm \
		-v ${PWD}:/work \
		-v ${PWD}/.tmp/online-judge-tools:/home/$(shell whoami)/.local/share/online-judge-tools/ \
		-v ${PWD}/.tmp/cargo-compete:/home/$(shell whoami)/.local/share/cargo-compete/ \
		-e "BROWSER=chrome" --name $(ATCODER_CONTAINER_NAME) $(ATCODER_NEW_IMAGE) bash && \
	clear && \
	docker exec -it $(ATCODER_CONTAINER_NAME) bash
else
run-atcoder:
	clear && \
	docker exec -it $(ATCODER_CONTAINER_NAME) bash
endif

stop-atcoder:
	docker stop $(ATCODER_CONTAINER_NAME)

run-test:
	docker run --rm -v ${PWD}:/work $(ATCODER_IMAGE) python algorithm_libraries/test/test.py

run-cpp-test:
	docker run --rm -v ${PWD}:/work $(ATCODER_IMAGE) python algorithm_libraries/test/test.py --lang=cpp

lint:
	docker run --rm -v ${PWD}:/work $(ATCODER_IMAGE) pysen run lint

auto-lint:
	docker run --rm -v ${PWD}:/work $(ATCODER_IMAGE) pysen run format

run-lint-generate:
	docker run --rm -v ${PWD}:/work $(ATCODER_IMAGE) pysen generate .
