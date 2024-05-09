from flask import render_template, request, redirect, url_for, Flask

from app.form import SearchForm
from app.services import get_all_rows_containing

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('search', text=request.form['searchbar']))
    return render_template('index.html', form=SearchForm())


@app.route('/search', methods=['POST'])
def search():
    rows = get_all_rows_containing(request.form['searchbar'])
    return render_template(
        'search.html',
        rows=rows[:100],
        amount_of_rows=len(rows),
    )
