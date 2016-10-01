#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',title="Titulo de la página")

if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)