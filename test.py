
from flask import Flask, render_template

app = flask(__name__)

@app.route ("/")
def "hello" ();
    return render_template('home.html')
