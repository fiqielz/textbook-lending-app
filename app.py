from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Pastikan name ditulis dengan benar

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_role', methods=['POST'])
def select_role():
    role = request.form.get('role')
    if role == 'teacher':
        return redirect(url_for('teacher'))
    else:
        return redirect(url_for('spbt'))

@app.route('/teacher')
def teacher():
    return "Selamat datang, Guru!"

@app.route('/spbt')
def spbt():
    return "Selamat datang, SPBT!"

if __name__ == '__main__':
    app.run(debug=True)
