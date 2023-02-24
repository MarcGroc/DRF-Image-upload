# Project Setup
- Clone project repository ``https://github.com/MarcGroc/recruitment_task.git``
- Create .env file in /deployment/local/ folder and add following variables
```
POSTGRES_SERVER=db
POSTGRES_USER=postgres
POSTGRES_DB=hexocean
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379

DJANGO_SUPERUSER_USERNAME="admin"
DJANGO_SUPERUSER_EMAIL="a@a.com"
DJANGO_SUPERUSER_PASSWORD="apitask123"
```

# Run project
- Run ``docker compose -f /deployment/local/docker-compose.yml up --build`` to build and run docker containers
- Go to ``http://localhost:8000/api`` to access api
- Login with ``admin`` user and password ``apitask123``
- Create tier in django admin panel (Basic, Premium, Enterprise)
- Assign tier to user in django admin panel (Account tiers)
- Now you can upload image and get response with image options at ``http://localhost:8000/api/image/``
- Response will be based on tier assigned to account 

# Detailed documentation
- Detailed documentation can be found in [docs](docs) folder.

# Time to complete task
- about 25 hours
