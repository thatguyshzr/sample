
import re
import numpy as np
import flask
from flask import Flask, request
import json

app= Flask(__name__)

@app.route('/home')  # decorator
def test_api():
    return 'Works.'

@app.route('/topwords', methods= ['POST'])  # decorator
def find_top_words():
    data= json.loads(request.data.decode())
    text, num_words= data['text'], data['num']
    print(data)
    
    word_tokens= re.split(' |;|,|:',text)
    word_len= [len(word) for word in word_tokens]
    print(word_len)
    
    sorted_len= np.argsort(word_len)
    top_words= []
    print(sorted_len)
    print(type(sorted_len))
    for idx in sorted_len[-int(num_words):]:
        top_words.append(word_tokens[idx])
    return str(top_words)

@app.route('/lastwords', methods= ['POST'])  # decorator
def find_last_words():
    data= json.loads(request.data.decode())
    text, num_words= data['text'], data['num']
    print(data)
    word_tokens= re.split(' |;|,|:',text)
    word_len= [len(word) for word in word_tokens]
    sorted_len= np.argsort(word_len)
    last_words= []
    for idx in sorted_len[:int(num_words)]:
        last_words.append(word_tokens[idx])
    return str(last_words)

if __name__ == '__main__':  # first thing that loads
    app.run(host= 'localhost', port= 8080)
    
'''
{
	"text": "Join 8 million developers and download the ONLY complete API Development Environment",
	"num":"2"
	
}
'''
    