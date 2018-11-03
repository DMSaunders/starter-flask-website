from flask import Flask,render_template, request, jsonify, Response
import pickle
import pandas as pd

app = Flask(__name__)   #init

@app.route('/', methods = ['GET'])  # home page. this is the URL on the webbrowser
def home():
    return render_template('home.html') #'<p> Hello World </p>'  #content

@app.route('/mpg', methods = ['GET'])  # mpg page
def mpg():
    return render_template('mpg.html') 

model = pickle.load(open('linreg.p', 'rb')) #load in the model

@app.route('/inference', methods = ['POST']) #create an inference route
def inference():
    req = request.get_json()
    print(req)
    c, h, w = req['cylinders'], req['horsepower'], req['weight']
    prediction = float(model.predict([[c,h,w]]))
    print(prediction)
    return jsonify({'c':c, 'h':h, 'w':w, 'prediction': prediction}) 

#route for plotting
@app.route('/plot', methods = ['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg,df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)



'''shift command R to full reload the webpage'''