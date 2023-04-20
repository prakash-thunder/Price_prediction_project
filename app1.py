from flask import Flask,request,render_template
import joblib
import sklearn
import numpy as np

def predict_price(LOC,SQFT,BATH,BHK): 
    __model=None
    x =np.array( ["total_sqft", "bath", "bhk", "7th phase jp nagar", "bannerghatta road", "electronic city", "electronic city phase ii", "haralur road", "hebbal", "hennur road", "kanakpura road", "marathahalli", "raja rajeshwari nagar", "rajaji nagar" ,"sarjapur  road", "thanisandra", "uttarahalli", "whitefield", "yelahanka"] )  
    try:
        loc_index = np.where(x==LOC)[0][0]
    except:
        loc_index = -1

    X = np.zeros(len(x))
    X[0] = SQFT
    X[1] = BATH
    X[2] = BHK
    if loc_index >= 0:
        X[loc_index] = 1
    return X #__model.predict([X])
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('tutorial.html')
@app.route('/predict',methods=['GET',"POST"])
def predict():
    if request.method=='POST':
        # __model=None
        x=["total_sqft", "bath", "bhk", "7th phase jp nagar", "bannerghatta road", "electronic city", "electronic city phase ii", "haralur road", "hebbal", "hennur road", "kanakpura road", "marathahalli", "raja rajeshwari nagar", "rajaji nagar", "sarjapur  road", "thanisandra", "uttarahalli", "whitefield", "yelahanka"]
    
        LOC=str(request.form['locat'])
        SQFT=int(request.form['total_sqft'])
        BATH=int(request.form["bath"]) 
        BHK=int(request.form["bhk"])
        # if __model is None:
        __model=joblib.load('banglore_home_prices_model100.pickle','rb')
            
        print("loading saved artifacts...done")
        print(LOC,SQFT,BATH,BHK)
        
        pred=(__model.predict([predict_price(LOC,SQFT,BATH,BHK)]))[0]
        print(pred)
        return render_template('tutorial.html',data=pred)
    else:
        return "Something went wrong"

if __name__=="__main__":
    app.run(debug=True)
