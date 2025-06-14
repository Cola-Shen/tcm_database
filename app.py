from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)  # 這行要放在最上面初始化

# 載入資料
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 首頁：查詢表單
@app.route('/')
def home():
    return render_template('index.html')

# 查詢功能：模糊搜尋
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

# 瀏覽功能：顯示全部資料
@app.route('/browse')
def browse():
    return render_template('browse.html', data=data)

if __name__ == '__main__':
    app.run()
