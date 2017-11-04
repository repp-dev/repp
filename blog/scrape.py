from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import os
import uuid
from twitter import *
twitter = Twitter(auth=OAuth("3432967618-K5tO2Vgwo61DNQAV8SPDCj9Uujk6mVNHIByGXQq", "iR4ZdwnikQnMiyTZMZ3PB614pDenqvmHEK7sHSgGnv0sJ", "yYu1Fst9rhsv0HeeZnIMhIu0d", "VFEHtj9yynT3htQ1K4w8xa2cGCLahXNz57k0w2cGkMcrNoz8Cr"))
    
url = os.environ.get('GRAPHENEDB_URL', 'http://repp.link:7474')
username = "neo4j"
password = "neo4jneo4j"

graph = Graph(url + '/db/data/', username=username, password=password)

def timestamp():
    epoch = datetime.utcfromtimestamp(0)
    now = datetime.now()
    delta = now - epoch
    return delta.total_seconds()

def date():
    return datetime.now().strftime('%Y-%m-%d')

def register(username, password):
        user = Node('User', username=username, password=bcrypt.encrypt(password))
        try:
            graph.create(user)
        except Exception, e:
            print "alreay have user: "+username
            
hashtagsToScrape = ["politics","metoo","apple", "trump"]
for tagToScrape in hashtagsToScrape:
    results = twitter.search.tweets(q=tagToScrape)
        
    for tweet in results['statuses']:
    
        tweetText = tweet['text'].encode('utf-8')
        tweetAuthor = tweet['user']['screen_name'].encode('utf-8')
        language = tweet['user']['lang'].encode('utf-8')
        if language != "en":
            continue
        if 'http' in tweetText:
            continue
    
        register(tweetAuthor, tweetAuthor+tweetAuthor)
        user = graph.find_one('User', 'username',tweetAuthor)
        
        post = Node(
            'Post',
            id=tweet['id'],
            title="Tweet",
            text=tweetText,
            timestamp=timestamp(),
            date=date()
        )
        rel = Relationship(user, 'PUBLISHED', post)
    
        try:
            graph.create(rel)
        except Exception, e:
            continue
    
        print "New Tweet ("+language+"): "+tweetAuthor+":"+tweetText
        for hashtag in tweet['entities']['hashtags']:
            tag = Node('Tag', name=hashtag['text'])
            graph.merge(tag)
            rel = Relationship(tag, 'TAGGED', post)
            graph.create(rel)
