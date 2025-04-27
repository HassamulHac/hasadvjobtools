# app.py
from flask import Flask, render_template
from tools.url_tool import url_tool_bp
from tools.json_to_csv import json_to_csv_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Register the Blueprints
app.register_blueprint(url_tool_bp, url_prefix='/url')
app.register_blueprint(json_to_csv_bp, url_prefix='/json-to-csv')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
