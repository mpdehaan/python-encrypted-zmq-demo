#!/usr/bin/python

import zmq
import json
from keyczar.keys import AesKey

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5099")

file = open('shared_secret.junk')
key = AesKey.Read(file.read())
 
for i in range(10):

    data = dict(
       operation="put",
       param1="alpha",
       param2="beta"
    )
    data = json.dumps(data)
    data = key.Encrypt(data)     

    socket.send(data)

    msg_in = socket.recv()

    data = key.Decrypt(data)
    print json.loads(data)
