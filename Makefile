lint: 
	black . --line-length=80

build:
	pip uninstall kafkademia -y
	rm -f dist/
	python setup.py sdist bdist_wheel