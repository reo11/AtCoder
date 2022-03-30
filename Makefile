ATCODER_IMAGE := atcoder:latest

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

.PHONY: build-atcoder
build-atcoder:
	docker build -t $(ATCODER_IMAGE) .

.PHONY: run-atcoder
run-atcoder: build-atcoder
	docker run -t -d --rm -v ${PWD}:/work -v ${PWD}/.tmp:/root/.local/share/online-judge-tools/ $(AUTO_LINT_IMAGE) -e "BROWSER=chrome" --name atcoder-container bash

.PHONY: exec-atcoder
exec-atcoder: 
	docker exec -it atcoder-container bash

