#!/usr/bin/python

import json
import urllib2
import sys

#listen_port=8888

if ((len(sys.argv) !=2)):
   print ("""This script required arithmetic sequence""")
   sys.exit(0)

input_seq = sys.argv[1]


#default dict:
data = {'arithmetic_seq':'0+0'}
#update dict with arg.:
data['arithmetic_seq'] = input_seq

host = 'http://127.0.0.1:8888/postcalc'
myrequest = urllib2.Request(host)
myrequest.add_header('Content-Type', 'application/json')

try:
   response = urllib2.urlopen(myrequest, json.dumps(data))
   result = json.load(response)
   print (result)
   response.close()
except urllib2.HTTPError as e:
      print ("HTTP Error ")
      print (e.getcode())
except urllib2.URLError as e:
      print ("URL Error ")
