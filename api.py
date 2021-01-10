from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json


app = Flask(__name__)


def load_dataset():
    global X_test
    global y_test
    # load csv x and y test
    X_test = pd.read_csv(
        "OnlineNewsPopularity/x_test.csv", sep=";")
    y_test = pd.read_csv(
        "OnlineNewsPopularity/y_test.csv", sep=";")

    # Delete first column of x_test
    first_column = X_test.columns[0]
    X_test = X_test.drop([first_column], axis=1)

    # Delete first column y_test
    first_column = y_test.columns[0]
    y_test = y_test.drop([first_column], axis=1)
    print(y_test.shape)


# Renvoi la prédiction de la popularité d'un article et si la prediction est bonne ou non
@app.route('/predict_popularity/<int:article_id>', methods=['GET'])
def make_prediction(article_id):
    print(model)
    article = X_test.iloc[article_id]
    prediction = model.predict([article])
    is_popular = y_test.iloc[article_id]
    print("is_popular ?")
    print(is_popular)
    print('-----')
    print('prediction')
    print(prediction[0])
    return jsonify({"prediction":  bool(prediction[0])}), 200


@app.route('/articles', methods=['GET'])
def get_articles_number():
    return jsonify({"articles_number": len(X_test.index)}), 200


if __name__ == '__main__':
    modelfile = 'models/best_model.pkl'
    model = p.load(open(modelfile, 'rb'))
    load_dataset()
    app.run(debug=True, host='0.0.0.0')
