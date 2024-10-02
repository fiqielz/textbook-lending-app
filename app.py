from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Textbook Lending App!"

if name == 'main':
    app.run(debug=True)
