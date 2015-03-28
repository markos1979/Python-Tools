#!/usr/bin/python
import codecs
import sys

def rot13(s):
	return codecs.encode(s, 'rot13') 


print "Text ciphered : " + sys.argv[1]
print "Test unciphered : " + rot13(sys.argv[1])

