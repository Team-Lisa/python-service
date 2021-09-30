build:
	docker build  . --rm -t app
start:
	docker run --rm -it -e PORT=3000 -e DB_PASSWORD=<password_db> --name app -p 3000:3000 app
test:
	docker build  -f Dockerfile.test . --rm  -t app-test
	docker run --rm -e DB_PASSWORD=<password_db> -it app-test