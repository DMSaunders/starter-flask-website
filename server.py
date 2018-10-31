from flask import Flask,render_template, request,jsonify,Response
import pickle
import pandas as pd

app = Flask(__name__)   #init

@app.route('/', methods = ['GET'])  # this is the URL on the webbrowser
def home():
    return render_template('home.html') #'<p> Hello World </p>'  #content


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)