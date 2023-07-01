
import numpy as np
import pickle
from flask import Flask,request, render_template

app=Flask(__name__,template_folder="templates")
model = pickle.load(open( 'D:/Python/Flask-UI/rf_rand_model.pkl','rb'))

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')
@app.route('/home', methods=['GET'])
def about():
    return render_template('home.html')
@app.route('/pred',methods=['GET'])
def page():
    return render_template('upload.html')
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    print(features_value)

    #features_name = ["city','BHKS', 'sqft_per_inch','build_up_ area', 'Type_ of_ property','deposit']
    prediction = model.predict(features_value)
    output=prediction[0]    #np.exp(predictions)
    output = np.exp(output)
    output = np.round(output)
    print(output)
    return render_template('upload.html', prediction_text= 'House Rent is {} '.format((output)))
    
    
if __name__  == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
