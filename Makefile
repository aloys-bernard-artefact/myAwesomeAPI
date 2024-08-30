

.PHONY: all 
all : black tests lint 


.PHONY: tests
tests : 
	@echo "Running tests"
	PYTHONPATH=. pytest -v

.PHONY: lint
lint : 
	@echo "Running lint"
	pylint --rcfile=.pylintrc src 

.PHONY: black
black : 
	@echo "Running black"
	black .
