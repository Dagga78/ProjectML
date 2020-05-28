import numpy as np
from flask import Flask, render_template, request
import os


app = Flask(__name__, template_folder='template')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def tweet():


    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=True,host='0.0.0.0',port=port)