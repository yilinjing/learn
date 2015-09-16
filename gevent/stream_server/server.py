#encoding=utf8
#!/bin/env python

from gevent import pool
from gevent.server import StreamServer
from gevent import Timeout
from gevent import sleep

def handle(sk, address):
    print 'new connection from {}'.format(address)
    sleep(60 * 10)
       
pool_size = 10
pl = pool.Pool(pool_size)
server = StreamServer(('127.0.0.1', 8081), handle, spawn=pl)
server.serve_forever()
