# Project Setup
- Clone project repository ``https://github.com/MarcGroc/recruitment_task.git``
- Run ``docker compose -f /deployment/local/docker-compose.yml up --build`` to build and run docker containers
- Go to ``http://localhost:8000/api`` to access api
- Login with ``admin`` user and password ``apitask123``
- Make POST request at to create Tier``http://localhost:8000/api/tier/`` (Basic, Premium, Enterprise)
- Make POST request at to assign Tier to Account``http://localhost:8000/api/account_tier/`` (Basic, Premium, Enterprise)
- Now you can upload image and get response with image options at ``http://localhost:8000/api/image/``

# Detailed documentation
- Detailed documentation can be found in [docs](docs) folder.
