build:
	docker build -t jobzback .

run:
	docker-compose up -d

stop:
	docker-compose down

backend:
	docker exec -it backend bash

db:
	docker exec -it db bash

migrate:
	docker exec -it backend python3 manage.py makemigrations
	docker exec -it backend python3 manage.py migrate