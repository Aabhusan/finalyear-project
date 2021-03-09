from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 
import pandas as pd 
import numpy as np 

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	df= pd.read_csv("./data/names_dataset.csv",usecols=[1,2])
	# Features and Labels
	df_X = df.name
	df_Y = df.sex
    
    # Vectorization
	corpus = df_X
	cv = CountVectorizer(analyzer='char_wb', ngram_range=(3, 3))
	X = cv.fit_transform(corpus) 
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	le.fit(['M','F'])
	y = le.transform(df_Y)

	# Loading our ML Model
	model= open("./model.pkl","rb")
	clf = joblib.load(model)

	# Receives the input query from form
	if request.method == 'POST':
		namequery = request.form['namequery']
		data = [namequery]
		vect = cv.transform(data)
		my_prediction = clf.predict(vect)
	return render_template('results.html',prediction = my_prediction,name = namequery.upper())


if __name__ == '__main__':
	app.run(debug=True)