import argparse
from nineteen898.twapi import TWAPI

def main():
    tw = TWAPI(config_file='config.yml')
    tw.get_()

if __name__ == '__main__':
    main()