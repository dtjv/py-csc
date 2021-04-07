install:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]
	then
		pip install -r requirements.txt
		precommit install
	fi

test:
	python -m unittest discover -s tests

lint:
	python -m flake8 .

format:
	autopep8 . --recursive --aggressive --aggressive --in-place --verbose
