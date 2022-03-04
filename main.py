from flask import Flask
from public import public
from admin import admin
from api import api
app=Flask(__name__)
app.secret_key="hh"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(api,url_prefix='/api')
# app.run(debug=True,port="5010",host="192.168.43.8")
app.run(debug=True,port="5011",host="192.168.83.145")
# app.run(debug=True,port="5010")