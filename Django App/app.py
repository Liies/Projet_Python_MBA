from flask import Flask, request, jsonify, render_template, url_for
from flask_bootstrap import Bootstrap
import pickle
import numpy as np

app = Flask(__name__)
Bootstrap(app)
model = pickle.load(open('./model/Paris prediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]

    surface_reelle_bati, nombre_pieces_principales, code_postal = int_features
   
    complete_features = [ surface_reelle_bati, nombre_pieces_principales, code_postal ] 
    final_features = [np.array(complete_features)]
    prediction = model.predict(final_features)

    output = prediction[0]


    return render_template('index.html', prediction_text='La valeur foncière de ce bien est: {} €'.format(round(output[0])))

if __name__ == "__main__":
    #démarre un serveur en local qui serve ma webapp
    print(app.url_map)
    app.run(host="127.0.0.1",port=5000,debug=True)