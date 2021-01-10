import requests
import json

url = 'http://127.0.0.1:5000/predict_popularity/'
headers = {'Accept-Charset': 'UTF-8'}
url1 = 'http://127.0.0.1:5000/max_article_nbr'
result = requests.get(url1, headers=headers)
max_range = json.loads(result.text)['articles_number']

while True:
    text = input("Select article number (between 0" + " and " +
                 str(max_range) + ") to predict: ")  # Python 3
    article_id = int(text)
    result = requests.get(url + str(article_id), headers=headers)
    print(result, result.text)
    """ result = requests.get(url1, headers=headers)
    print(result, result.text) """
