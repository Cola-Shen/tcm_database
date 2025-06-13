# app.py:負責網站邏輯與資料讀取
# data.json:用來儲存中醫資料
# index.html:建立網頁查詢系統

from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    query = ''

    if request.method == 'POST':
        query = request.form.get('keyword', '').strip()
        data = load_data()

        # 以不區分大小寫比對 keyword
        for entry in data:
            if entry['keyword'].lower() == query.lower():
                result = entry
                break

    return render_template('index.html', query=query, result=result)

if __name__ == '__main__':
    app.run(debug=True)
