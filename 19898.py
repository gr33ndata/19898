import sys
import json
import argparse
from nineteen898.twapi import TWAPI

def show_version():
    from nineteen898 import version
    print version.__version__

def get_tweets(query='', count=100):
    tw = TWAPI(config_file='config.yml')
    return tw.get_tweets(query=query, count=count)

def save_to_file(filename='', posts=[]):
    fd = open(filename,'w')
    json_data = {"data": posts}
    json.dump(json_data, fd)
    fd.close()

def dump_to_screen(posts=[]):
    json_data = {"data": posts}
    print json.dumps(json_data)

def main():
    parser = argparse.ArgumentParser(description='CLI tool for social media data analysis')
    parser.add_argument('source', choices=['twitter'], default='twitter', help='Social network to get data from')
    parser.add_argument('-q', '--query', metavar='Query', default='#OpenData', help='Query used to get the data based on')
    parser.add_argument('-c', '--count', metavar='Count', default=100, help='Number of posts to retrieve')
    parser.add_argument('-o', '--output', metavar='OutputFile', default='', help='Dump data to filename specified by OutputFile')
    parser.add_argument('-v', '--verbose', metavar='Verbose', nargs='?', const=True, default=False, help='Show debug messages')
    args = parser.parse_args()
    
    if args.verbose: 
        print args

    count = int(args.count)
    posts = get_tweets(query=args.query, count=count)
    
    if args.verbose: 
        print len(posts)
        for post in posts:
            print post["id"]
    
    if args.output:
        save_to_file(args.output, posts)
    else:
        dump_to_screen(posts)

if __name__ == '__main__':
    main()