FROM ubuntu:14.04
MAINTAINER Phillip Bailey <phillip@bailey.st>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python git \
    nginx supervisor
COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app /var/www/app

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    &&  pip install -r /var/www/app/requirements.txt \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log
RUN git clone https://github.com/Backfeed/backfeed-protocol.git
RUN pip install backfeed-protocol/
RUN pip install --upgrade pip
RUN sudo -E pip install bcrypt
EXPOSE 80
CMD [ "python", "/var/www/neo4j/run.py" ]
