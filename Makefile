ATCODER_IMAGE := atcoder:latest
TEST_IMAGE := actoder-test:latest

.PHONY: help
help: ## this is help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean-pyc

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: build-test
build-test:
	docker build --build-arg UID=$(shell id -u) --build-arg UNAME=$(shell whoami) -t $(TEST_IMAGE) -f dockerfiles/Dockerfile.test .

.PHONY: run-test
run-test: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pytest test/*

.PHONY: run-lint
run-lint: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen run lint

.PHONY: run-auto-lint
run-auto-lint: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen run format

.PHONY: run-lint-generate
run-lint-generate: build-test
	docker run --rm -v ${PWD}:/work $(TEST_IMAGE) pysen generate .

.PHONY: build-atcoder
build-atcoder:
	docker build -t $(ATCODER_IMAGE) .

.PHONY: run-atcoder
run-atcoder: build-atcoder
	docker run -t -d --rm -v ${PWD}:/work -v ${PWD}/.tmp:/root/.local/share/online-judge-tools/ $(ATCODER_IMAGE) -e "BROWSER=chrome" --name atcoder-container bash

.PHONY: exec-atcoder
exec-atcoder: 
	docker exec -it atcoder-container bash

