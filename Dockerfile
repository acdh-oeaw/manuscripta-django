# Dockerfile
# https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
# chmod 755 start-server.sh
FROM python:3.7-buster

# install nginx
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install nginx vim postgresql-common libpq-dev python3-gdal -y
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/djangobaseproject
COPY requirements.txt start-server.sh /opt/app/
COPY . /opt/app/djangobaseproject/
WORKDIR /opt/app
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn --no-cache-dir
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
