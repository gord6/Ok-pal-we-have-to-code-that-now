# Application for data collection

This directory contains the application that was used to collect the data. We provide the flask application in a containerized version in a development and production setup using docker-compose.  

### Development Setup
To run the application in development mode with hot reload locally, use the following command. The database will be rebuild for every restart using the data provided in `core/db_setup/db_setup_dev.json`.
You can access the application running on 127.0.0.1:5123 in your browser and log in using "admin" and password "password".

```bash
docker-compose -f docker-compose-dev.yaml up
```

### Production Setup
You might want to contact the authors if you want to make changes for data collection. 

Adjust the .env file with the following variables for the production setup:
```
STAGE=prod
PROXY_PATH_PREFIX="your_prefix"
```
The proxy path prefix can be set if a proxy server with a path prefix is used else add an empty string. 
You further need to add a `core/db_setup/db_setup_prod.json` containing your initialization  data. 
You can build and run the app on port 5000 using the following command:
```bash
docker-compose up --build -d
```
The data in the database will be saved on your servers filesystem in a `data` directory. That way, data persistence is ensured in case of a restart of the container. Don't change the permissions or content of the `data`` dir.