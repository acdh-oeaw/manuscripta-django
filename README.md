# hofburg

## docker

build the image with `docker build -t hofburg .`

provide a .env file with
```
DB_NAME=db-name
DB_USER=asdf
DB_PASSWORD=asdf
PROJECT_NAME=nomythdbapp
SECRET_KEY=hansi4ever
```
run the container with `docker run -it -p 8020:8020 --rm --env-file .env_dev hofburg`
