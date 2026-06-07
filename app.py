import flask
import time 
import os
import signal 

app=flask.Flask(__name__)

start_time=time.time()

@app.route('/uptime',methods=["GET"])
def return_uptime():
   end_time=time.time()
   uptime=end_time-start_time
   return flask.jsonify({"status":"UP","uptime": uptime})


@app.route("/kill",methods=["GET"])
def kill_process():
   process_id=os.getpid()
   os.kill(process_id,signal.SIGINT) 
   return flask.jsonify({"message":"shutting down the process"})

app.run(host="0.0.0.0",port="5000")
