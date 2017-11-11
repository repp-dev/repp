from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid

url = os.environ.get('GRAPHENEDB_URL', 'http://repp.link:7474')
username = "neo4j"
password = "neo4jneo4j"

graph = Graph(url + '/db/data/', username=username, password=password)

class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.find_one('User', 'username', self.username)
        return user

    def register(self, password):
        if not self.find():
            user = Node('User', username=self.username, password=bcrypt.encrypt(password))
            graph.create(user)
            return True
        else:
            return False

    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False

    def add_post(self, title, tags, text):
        user = self.find()
        post = Node(
            'Post',
            id=str(uuid.uuid4()),
            title=title,
            text=text,
            timestamp=timestamp(),
            date=date()
        )
        rel = Relationship(user, 'PUBLISHED', post)
        graph.create(rel)

        tags = [x.strip() for x in tags.lower().split(',')]
        for name in set(tags):
            tag = Node('Tag', name=name)
            graph.merge(tag)

            rel = Relationship(tag, 'TAGGED', post)
            graph.create(rel)
    
    def rate_authenticity(self, post_id,rating):
        user = self.find()
        post = graph.find_one('Post', 'id', post_id)
        graph.merge(Relationship(user, 'RATED_AUTHENTICITY', post , rating = rating))
    
    def rate_valid(self, post_id,rating):
        user = self.find()
        post = graph.find_one('Post', 'id', post_id)
        graph.merge(Relationship(user, 'RATED_VALID', post , rating = rating))

    def rate_like(self, post_id,rating):
        user = self.find()
        post = graph.find_one('Post', 'id', post_id)
        graph.merge(Relationship(user, 'RATED_LIKE', post , rating = rating))

    def rate_trust(self, post_id,rating):
        user = self.find()
        post = graph.find_one('Post', 'id', post_id)
        graph.merge(Relationship(user, 'RATED_TRUST', post , rating = rating))

    def get_recent_posts(self):
        query = '''
        MATCH (user:User)-[:PUBLISHED]->(post:Post)
        WHERE user.username = {username}
        RETURN post
        ORDER BY post.timestamp
        '''

        return graph.run(query, username=self.username)

def get_posts():
    query = '''
    MATCH (user:User)-[:PUBLISHED]->(post:Post)
    OPTIONAL MATCH (:User{ username: 'bruce' })-[trust:RATED_TRUST]->(post)
    OPTIONAL MATCH (:User{ username: 'bruce' })-[like:RATED_LIKE]->(post)
    OPTIONAL MATCH (:User{ username: 'bruce' })-[authenticity:RATED_AUTHENTICITY]->(post)
    OPTIONAL MATCH (:User{ username: 'bruce' })-[valid:RATED_VALID]->(post)
    RETURN user.username AS username, post, trust, like, authenticity,valid
    ORDER BY post.timestamp DESC LIMIT 200
    '''
    print('getting front page content')
    return graph.run(query, today=date())

def timestamp():
    epoch = datetime.utcfromtimestamp(0)
    now = datetime.now()
    delta = now - epoch
    return delta.total_seconds()

def date():
    return datetime.now().strftime('%Y-%m-%d')
