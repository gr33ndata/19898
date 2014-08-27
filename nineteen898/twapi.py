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
        self.key = conf['APIKey']
        self.secret = conf['APISecret'] 
        fd.close()
        self.get_bearer_token()

    def show_conf(self):
        print 'Twitter Key: ' + self.key 
        print 'Twitter Secret: ' + self.secret
        print 'Twitter Bearer Token: ' + self.bearer

    def get_bearer_token(self):
        self.bearer = base64.b64encode('%s:%s' % (self.key, self.secret))


    def search(self, query='', token=''):
        url = 'https://api.twitter.com/1.1/search/tweets.json'
        headers = {
            'Authorization': 'Bearer ' + token
        }
        payload = {
            'q': query
        }
        r = requests.get(url, params=payload, headers=headers)
        print r, r.text
        return r.json()

    def get_(self, query=''):
        
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
            return self.search(query=query, token=token)
        else:
            print r.status_code

if __name__ == '__main__':
    tw = TWAPI()
    tw.get_()