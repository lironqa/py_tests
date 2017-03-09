#!/usr/bin/python
import json

listen_port = 8888
calcs_q_list = [];
calcs_a_list = [];
dicta={}

from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def index():
   return "Hello, Python server is up. Please use POST method to calcstr\n"

@app.route('/calc')

def calc():
   if 'calcstr' in request.args:
      math_result = eval(request.args['calcstr'])
      calcs_q_list.append(str(request.args['calcstr']))
      calcs_a_list.append(str(math_result))
      return str(math_result)
   else:
      return "Unable to calc' this\n"  


@app.route('/postcalc', methods=['POST']) 
def postcalc():
   if request.method == 'POST':
      jsonreq = request.json['arithmetic_seq']
      result_str = str(eval(jsonreq))
      calcs_q_str = (str(jsonreq))
      calcs_a_str = (result_str)
      dicta[calcs_q_str]=calcs_a_str
      print_result_str = result_str+'\n'
      return print_result_str


@app.route('/getcalc', methods=['GET'])
def getcalc():
   if request.method == 'GET':
      r=json.dumps(dicta)
      print r
      r+='\n'
      return r

@app.route ('/ver',methods=['GET'])
def prntver():
    if request.method == 'GET':
      return "ver=1.0\n"

 

if __name__ == '__main__':
   app.run(port=listen_port,debug=True)

