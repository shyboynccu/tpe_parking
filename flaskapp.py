import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

@app.route("/map")
def mark_my_map():
    return render_template('map.html', coord = {'pos': [25.041340, 121.611751]})

@app.route("/m.map")
def mark_my_mobile_map():
    return render_template('m.map.html')

if __name__ == '__main__':
    app.run()
