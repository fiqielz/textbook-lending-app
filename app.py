from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Textbook Lending App!"

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/admin')
def admin():
    return '''
    <h1>Admin Page</h1>
    <p>Record Returns/Loans of Textbooks</p>
    <!-- Anda boleh menambah lebih banyak ciri di sini -->
    '''
    @app.route('/teacher')
def teacher():
    return '''
    <h1>Teacher Page</h1>
    <p>Record Loans/Returns of Books</p>
    <!-- Anda boleh menambah lebih banyak ciri di sini -->
    '''
