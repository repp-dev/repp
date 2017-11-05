# ssh into ec2 instance
ssh -i /Users/r00t/Downloads/repp_norcal.pem ubuntu@ec2-54-153-107-211.us-west-1.compute.amazonaws.com`

# nginx proxy
sudo docker run -d -p 80:80 --name proxy -e DEFAULT_HOST=repp.link -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy

# create cloud9
sudo docker run -d -v ~/:/workspace --name cloud9 -e VIRTUAL_HOST=cloud9.repp.link -P sapk/cloud9 --auth username:password

# create neo4j database
sudo docker run -i -t -d --name neo4j --cap-add=SYS_RESOURCE -e VIRTUAL_HOST=neo4j.repp.link -p 7474:7474 -e NEO4J_AUTH=neo4j:neo4jneo4j tpires/neo4j

# create flask container
sudo docker run -d --name flask -v /home/ubuntu/repp:/var/www/neo4j -e VIRTUAL_HOST=app.repp.link repp/flask

# attach to python server
sudo docker exec -it flask bash
