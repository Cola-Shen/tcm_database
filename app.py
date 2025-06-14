# app.py:負責網站邏輯與資料讀取
# data.json:用來儲存中醫資料
# index.html:建立網頁查詢系統

from flask import Flask, request, render_template
import json

app = Flask(__name__)

# 載入資料
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('q', '').lower()
    results = [
        item for item in data
        if keyword in item['keyword'].lower()
           or keyword in item['TCM']['description'].lower()
           or keyword in item['Med']['description'].lower()
    ]
    return render_template('index.html', results=results, query=keyword)

if __name__ == '__main__':
    app.run()
