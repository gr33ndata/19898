import os 
import json
import yaml
import base64
import requests

class TWAPI:
    
    def __init__(self, config_file='../config.yml'):
        #print os.getcwd()
        self.config_file = config_file
        self.key = ''
        self.secret = ''
        self.bearer = ''
        self.load_conf()
        #self.show_conf()

    def load_conf(self):
        fd = open(self.config_file, 'r')
        conf = yaml.load(fd)
        self.key = conf['TwitterKey']
        self.secret = conf['TwitterSecret'] 
        fd.close()
        self.get_bearer_token()

    def show_conf(self):
        print 'Twitter Key: ' + self.key 
        print 'Twitter Secret: ' + self.secret
        print 'Twitter Bearer Token: ' + self.bearer

    def get_bearer_token(self):
        self.bearer = base64.b64encode('%s:%s' % (self.key, self.secret))


    def search(self, query='', token='', max_posts=100, max_id=0):
        if max_posts == 0:
            return []
        count = min(max_posts, 100)
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        headers = {
            'Authorization': 'Bearer ' + token
        }
        payload = {
            'result_type': 'recent',
            'q': query,
            'count': count,
            'max_id': max_id
        }
        ret_data = []
        r = requests.get(url, params=payload, headers=headers)
        #print r, r.text
        if r.status_code == 200:
            ret_data = [status for status in r.json()["statuses"]]
            max_id = int(ret_data[-1]["id"]) - 1
            ret_data = ret_data + self.search(query=query, token=token, max_posts=max_posts-count, max_id=max_id)     
        return ret_data

    def get_tweets(self, query='', count=100):
        
        url = 'https://api.twitter.com/oauth2/token'
        payload = {
            'grant_type': 'client_credentials'
        }
        headers = {
            'Authorization': 'Basic ' + self.bearer,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }

        r = requests.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            token = r.json()["access_token"]
            return self.search(query=query, token=token, max_posts=count)
        else:
            print r.status_code

    def get_user(self, user='', count=10):
        
        url = 'https://api.twitter.com/oauth2/token'
        payload = {
            'grant_type': 'client_credentials'
        }
        headers = {
            'Authorization': 'Basic ' + self.bearer,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }

        r = requests.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            token = r.json()["access_token"]
            #return self.search(query='@{}'.format(user), token=token, max_posts=count)
            return user
        else:
            print r.status_code

if __name__ == '__main__':
    tw = TWAPI()
    tw.get_()