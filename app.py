# app.py
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model/fake_news_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        news_text = request.form['news']
        prediction = model.predict([news_text])
        result = f"The news is likely: {prediction[0]}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
