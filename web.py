from os import urandom

from flask import render_template, request, redirect, url_for, Flask
from flask_bootstrap import Bootstrap5

from app.form import SearchForm
from app.services import get_all_rows_containing

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(32)
bootstrap = Bootstrap5(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('search', text=request.form['search']))
    return render_template('index.html', form=SearchForm())


@app.route('/search', methods=['GET'])
def search():
    text = request.args.get('text')
    rows = get_all_rows_containing(text)
    return render_template(
        'search.html',
        rows=rows[:100],
        amount_of_rows=len(rows),
    )
