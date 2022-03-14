build:
	docker build -t jobzback .
run:
	docker container rm -f db
	docker container rm -f backend
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

#admin:
#	docker exec -it backend echo "from user.models import Person; Person.objects.create_superuser('admin', 'admin', '123', '123', 'admin@example.com', '12345')" | python3 manage.py shell

#provider:
#	docker exec -it backend echo "from user.models import Provider; Provider.objects.create_superuser('admin', 'admin', '123', '123', 'admin@example.com', '12345')" | python3 manage.py shell

