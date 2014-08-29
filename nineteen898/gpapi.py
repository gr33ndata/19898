import os 
import json
import yaml
import requests

class GPAPI:

    def __init__(self, config_file='../config.yml'):
        #print os.getcwd()
        self.config_file = config_file
        self.key = ''
        self.load_conf()
        #self.show_conf()

    def load_conf(self):
        fd = open(self.config_file, 'r')
        conf = yaml.load(fd)
        self.key = conf['GoogleKey']
        fd.close()