# Makefile
install:
	pip install -r requirements.txt
run:
	python setup.py install
	 python -m hydra