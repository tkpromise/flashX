from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username']!='admin' or request.form['password']!='secret':
            flash('faild')
        else:
            flash('successful!')
            return redirect(url_for('index'))
    return render_template('login.html')
