# ssh into ec2 instance
sudo ssh -i /Users/r00t/Downloads/repp_dev.pem ubuntu@ec2-52-53-211-225.us-west-1.compute.amazonaws.com

# nginx proxy
sudo docker run -d -p 80:80 --name proxy -e DEFAULT_HOST=repp.link -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy

# create cloud9
sudo docker run -d -v ~/:/workspace --name cloud9 -e VIRTUAL_HOST=cloud9.repp.link -P sapk/cloud9 --auth username:password

# create neo4j database
sudo docker run -i -t -d --name neo4j --cap-add=SYS_RESOURCE -p 7474:7474 -e NEO4J_AUTH=neo4j:neo4jneo4j tpires/neo4j

# create flask container
#sudo docker run -d --name flask -v /home/ubuntu/repp/blog:/var/www/app -e VIRTUAL_HOST=app.repp.link -P p0bailey/docker-flask
sudo docker run -d --name flask -v /home/ubuntu/repp:/var/www/app -e VIRTUAL_PROTO=uwsgi -e VIRTUAL_HOST=app.repp.link -P p0bailey/docker-flask

# attach to container
sudo docker exec -it flask bash

# determine process number using port 80
netstat -tulpn

# get python install ready
pip install py2neo
sudo pip install passlib
sudo pip install uwsgi
pip install cryptography
sudo -E pip install bcrypt