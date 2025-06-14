# app.py:負責網站邏輯與資料讀取
# data.json:用來儲存中醫資料
# index.html:建立網頁查詢系統

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 讀取中西整合資料庫 JSON
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/search')
def search():
    keyword = request.args.get('q', '').lower()

    # 使用模糊查詢（包含關鍵字即符合）
    results = [item for item in data if keyword in item['name'].lower() or keyword in item.get('description', '').lower()]

    return jsonify(results)

if __name__ == '__main__':
    app.run()
