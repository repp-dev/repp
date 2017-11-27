from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid

url = os.environ.get('GRAPHENEDB_URL', 'http://neo4j')
username = "neo4j"
password = "neo4jneo4j"

graph = Graph(url + '/db/data/', username=username, password=password)

for action in graph.run('MATCH (user)-[rating:RATED_AUTHENTICITY]->(post) RETURN rating, user, post'):
    print(action['user']['username'] )
    print (action['rating']['rating'])
    print (action['post']['id'])
    print (action['post']['author'])
    print ("------ AUTHENTICITY")
    
for action in graph.run('MATCH (user)-[rating:RATED_TRUST]->(post) RETURN rating, user, post'):
    print(action['user']['username'] )
    print (action['rating']['rating'])
    print (action['post']['id'])
    print (action['post']['author'])
    print ("------ TRUST")
    
for action in graph.run('MATCH (user)-[rating:RATED_VALID]->(post) RETURN rating, user, post'):
    print(action['user']['username'] )
    print (action['rating']['rating'])
    print (action['post']['id'])
    print (action['post']['author'])
    print ("------ VALID")
    
for action in graph.run('MATCH (user)-[rating:RATED_LIKE]->(post) RETURN rating, user, post'):
    print(action['user']['username'] )
    print (action['rating']['rating'])
    print (action['post']['id'])
    print (action['post']['author'])
    print ("------ LIKE")