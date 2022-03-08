build:
	docker build -t jobzback .
run:
	docker-compose up -d

stop:
	docker-compose down

