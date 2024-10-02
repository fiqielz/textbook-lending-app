from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/')
def home():
    return "Welcome to the Textbook Lending App!"

if name == 'main':
    app.run(debug=True)
