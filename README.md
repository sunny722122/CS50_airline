# CS50_airline
EDX CS50 course practice 

create dockerfile
create docker-compose.yml file
project setting.py
change database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

docker ps
lookup the container ID
run interactive bash command in container
docker exec -it containerID bash -l
then could run command in container
ctrl+D logout container


issue:
django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'
solution:
https://djangoforprofessionals.com/postgresql/
docker-compose up -d
docker-compose exec web pipenv install psycopg2-binary==2.8.5
issue:
Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.
solution
add 0.0.0.0 to allowedhost in project settings.py
ALLOWED_HOSTS = ['localhost', '127.0.0.1','0.0.0.0']
issue:
database connection problem, table has no relationship
solution:
docker-compose up -d
docker-compose exec web python manage.py migrate

if create superuser in docker
docker-compose exec web python manage.py createsuperuser
