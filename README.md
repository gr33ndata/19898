19898
=====

19898 or 19TWT is a CLI for downloading tweets, and in future we are goint to add support for Facebook, Google Plus, Last.fm, etc.

Usage:

You first need to rename `config.yml.example` into `config.yml`, then add your twitter key and secret there. After that, the CLI is as follows:

`python 19898.py [-h] [-q Query] [-c Count] [-o OutputFile] [-v [Verbose]] {twitter}`

CLI options

```
positional arguments:
  {twitter}             Social network to get data from

optional arguments:
  -h, --help            show this help message and exit
  -q Query, --query Query
                        Query used to get the data based on
  -c Count, --count Count
                        Number of posts to retrieve
  -o OutputFile, --output OutputFile
                        Dump data to filename specified by OutputFile
  -v [Verboce], --verbose [Verboce]
                        Show debug messages
```

Contacts
--------
 
+ Name: [Tarek Amr](http://tarekamr.appspot.com/)
+ Twitter: [@gr33ndata](https://twitter.com/gr33ndata)