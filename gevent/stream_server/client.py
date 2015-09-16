#!/bin/env python
#encoding=utf8

import socket
import os, sys
import concurrent.futures

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

host = "127.0.0.1"
port = 8081

def SendRequest(cnt):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #connect failed,then raise except
    try:
        sk.connect((host, port))    
    except:
        print 'connect failed'
        return
    
    print 'send request to {}:{} cnt:{}'.format(host, port, cnt)
    print sk.getsockname()
    sk.sendall('hello')
    while True:
        data = sk.recv(65536)
        if not data: 
            break
        
    sk.close()

with concurrent.futures.ProcessPoolExecutor(10) as executor:
    cnt = 0
    while cnt < 100:
        executor.submit(SendRequest, cnt)
        cnt += 1
