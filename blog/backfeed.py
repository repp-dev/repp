from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid

url = os.environ.get('GRAPHENEDB_URL', 'http://neo4j')
username = "neo4j"
password = "neo4jneo4j"

graph = Graph(url + '/db/data/', username=username, password=password)

query = 'MATCH (user)-[rating:RATED_AUTHENTICITY]->(post) RETURN rating, user, post'

actions = graph.run(query)
    
for action in actions:
    print(action['user']['username'] )
    print (action['rating']['rating'])
    print (action['post']['id'])
    print (action['post']['author'])
    print ("------")