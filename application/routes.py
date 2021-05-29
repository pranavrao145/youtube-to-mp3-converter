from application import app
from flask import render_template
from application import utils
from application.forms import SearchForm

@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        search = form.query.data
        response = utils.getSearches(search)
        return render_template("home.html", title="Home", items=response, form=form)
    return render_template("home.html", title="Home", form=form)

