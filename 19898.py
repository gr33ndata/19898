import argparse
from nineteen898.twapi import TWAPI

def show_version():
    from nineteen898 import version
    print version.__version__

def get_tweets(query=''):
    tw = TWAPI(config_file='config.yml')
    tw.get_(query=query)

def main():
    parser = argparse.ArgumentParser(description='CLI tool for social media data analysis')
    parser.add_argument('source', choices=['twitter'], default='twitter', help='Social network to get data from')
    parser.add_argument('-q', '--query', metavar='Query', default='1984', help='Query used to get the data based on')
    parser.add_argument('-o', '--output', metavar='OutputFile', default='output.json', help='Dump data to filename specified by OutputFile')
    args = parser.parse_args()
    print args

    get_tweets(query=args.query)
    

if __name__ == '__main__':
    main()