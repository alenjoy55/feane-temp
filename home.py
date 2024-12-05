from flask import Flask,render_template
import sqlite3


app=Flask(__name__)


@app.route('/')
def fun1():
    return render_template('index.html')

@app.route('/fun2')
def fun2():
    return render_template('about.html')

app.run()