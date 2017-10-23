# ssh into ec2 instance
sudo ssh -i /Users/r00t/Downloads/repp_dev.pem ubuntu@ec2-52-53-211-225.us-west-1.compute.amazonaws.com

#create cloud9
sudo docker run -d -v ~/:/workspace --name cloud9 -p 8181:8181 sapk/cloud9 --auth username:password

#create neo4j database
sudo docker run -i -t -d --name neo4j --cap-add=SYS_RESOURCE -p 7474:7474 tpires/neo4j

#create flask container
sudo docker run -d --name flask -v /home/ubuntu/repp/blog:/var/www/app -p 80:80 p0bailey/docker-flask
sudo docker run -d --name flask -v /home/ubuntu/repp:/var/www/neo4j -p 80:80 p0bailey/docker-flask

# attach to container
sudo docker exec -it 5c9a6b12a51d bash


netstat -tulpn


pip install py2neo
sudo pip install passlib
sudo pip install uwsgi
pip install cryptography
sudo -E pip install bcrypt