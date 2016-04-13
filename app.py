from flask import Flask

app = Flask(__name__) #corresponds to name of file you are in -- name app 

@app.route('/')
def hello():
    return 'Hello World'

app.run(host='0.0.0.0')#tells outside machine to allow outside requests because this is happening over a network aka VM

