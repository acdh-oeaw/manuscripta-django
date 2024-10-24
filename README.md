# manuscripta

### building the image

* `docker build -t manuscripta:latest .`
* `docker build -t manuscripta:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it --rm --network="host" --env-file .env_dev --name manuscripta manuscripta:latest` and open http://127.0.0.1:8020/
