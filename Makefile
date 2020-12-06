# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


SHELL=/bin/bash


BUILD=./build
DEVPI_USER=pr3d4t0r
DEVPI_PASSWORD=nopasswordsetyet
DIST=./dist
MODULE=$(shell cat modulename.txt)
# Preparation for devpi?
# REQUIREMENTS=$(shell cat requirements.txt)
REQUIREMENTS=requirements.txt
VERSION=$(shell cat version.txt)


# Targets:

all: ALWAYS
	make test
	make module
	make publish


clean:
	rm -Rf $(BUILD)/*
	rm -Rf $(DIST)/*
	rm -Rfv $$(find ./aoc | awk '/__pycache__$$/')
	rm -Rfv $$(find test | awk '/__pycache__$$/')
	rm -Rfv $$(find . | awk '/.ipynb_checkpoints/')
	rm -fv $(find . | awk '/bogus/')
	pushd ./resources ; pip uninstall -y $(MODULE)==$(VERSION) || true ; popd
    

install:
	pushd resources/ && pip install -e .. && popd
	pip list | awk 'NR < 3 { print; } /$(MODULE)/'


module:
	pip install -r $(REQUIREMENTS)
	python setup.py bdist_wheel


nuke: ALWAYS
	make clean
	rm -Rf $(shell find $(MODULE) | awk '/__pycache__$$/')
	rm -Rf $(shell find test/ | awk '/__pycache__$$/')


publish:
	@echo "publishing NOOP"


refresh: ALWAYS
	conda install mkl-service
	pip install -U -r requirements.txt


# Delete the Python virtual environment - necessary when updating the
# host's actual Python, e.g. upgrade from 3.7.5 to 3.7.6.
resetpy: ALWAYS
	rm -Rfv ./.Python ./bin ./build ./dist ./include ./lib


#	for f in aoc/*; do mypy "$$f"; done
test: ALWAYS
	pip install -r requirements.txt
	pip install -e .
	pytest -v ./test/test-boardingpass.py
	pytest -v ./test/test-expenses.py
	pytest -v ./test/test-passportscanner.py
	pytest -v ./test/test-trees.py
	pytest -v ./test/test-util.py
	pytest -v ./test/test-validate.py
	pytest -v ./test/test-customforms.py
	pip uninstall -y $(MODULE)==$(VERSION) || true
	rm -Rfv $$(find $(MODULE) | awk '/__pycache__$$/')
	rm -Rfv $$(find ./aoc | awk '/__pycache__$$/')
	rm -Rfv $$(find test | awk '/__pycache__$$/')


ALWAYS:

