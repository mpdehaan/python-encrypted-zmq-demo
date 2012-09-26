#!/usr/bin/python

import zmq
import json
from keyczar.keys import AesKey

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5099")

file = open('shared_secret.junk')
key = AesKey.Read(file.read())
 
while True:

    data = socket.recv()
    data = key.Decrypt(data)
    data = json.loads(data)

    operation = data['operation']
    param1    = data['param1']
    param2    = data['param2']

    print "Got", data

    data2 = json.dumps(data)
    data2 = key.Encrypt(data2)

    socket.send(data2)
