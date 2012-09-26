#!/usr/bin/python

from keyczar.keys import AesKey
k = AesKey.Generate()
print str(k)

