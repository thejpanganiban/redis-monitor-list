#!/usr/bin/env python
import redis
import os
import sys


HELP = 'Usage: python monitor_list.py [list]'
REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))
if len(sys.argv) != 2:
    print >> sys.stderr, HELP
    sys.exit(1)
QUEUE = sys.argv[1]


try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    print >> sys.stdout, r.llen(QUEUE)
except redis.ConnectionError:
    print >> sys.stdout, 'UNABLE TO CONNECT'
