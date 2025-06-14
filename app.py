from flask import Flask, request, render_template
import json

app = Flask(__name__)

# 載入資料
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('data_herbs.json', 'r', encoding='utf-8') as f:
    herb_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('q', '').lower()
    results = []

    for item in data:
        if (keyword in item['keyword'].lower() or
            keyword in item['TCM']['description'].lower() or
            keyword in item['Med']['description'].lower()):
            results.append(item)

    for category in herb_data:
        for herb in category.get('herbs', []):
            if (keyword in herb.get('name', '').lower() or
                keyword in herb.get('description', '').lower() or
                keyword in herb.get('usage', '').lower()):
                results.append({
                    'keyword': herb.get('name'),
                    'TCM': {
                        'type': '中藥',
                        'description': herb.get('description', ''),
                        'treatment': herb.get('usage', '')
                    },
                    'Med': {
                        'type': '',
                        'description': '',
                        'treatment': ''
                    }
                })
