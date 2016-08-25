from flask import Flask, render_template
from flask_flatpages import FlatPages
from vcscan import get_pokes, get_occur_dict
from datetime import datetime
import pdb
import sqlite3

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
pages = FlatPages(app)

@app.route('/')
def index():
	conn = sqlite3.connect("pogom_vc.db")
	occurDict = get_occur_dict(conn)
	pokespawns = get_pokes(conn)
	currents = [x for x in pokespawns if x.expiry_time > datetime.now()]
	return render_template('index.html', pages=pages, occurrences=occurDict, spawns=pokespawns, currents=currents)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(port=8000)