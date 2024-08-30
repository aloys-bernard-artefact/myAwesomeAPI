

.PHONY: all 
all : black tests lint 

# Testing & Linting

.PHONY: tests
tests : 
	@echo "Running tests"
	PYTHONPATH=. pytest -v

.PHONY: lint
lint : 
	@echo "Running lint"
	pylint --rcfile=.pylintrc src 

.PHONY: format
format : 
	@echo "Running black"
	black .


# Dependencies

install : 
	pip install --upgrade pip
	pip install -r requirements.txt
