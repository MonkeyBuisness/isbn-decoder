all: run

run:
	python3 ./app/main.py --f ./test.jpg

build:
	docker build -t isbn-decoder .

run-from-docker:
	docker run -i --rm --privileged=true -v ${PWD}/:/tmp isbn-decoder --f "/tmp/test.jpg"
