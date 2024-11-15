import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .validators import letters_validator


ROW_SIZE = 6


def get_unique_short_id():
    rand_string = ''.join(random.sample(string.digits + string.ascii_letters, ROW_SIZE))
    return rand_string


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        new_href = form.custom_id.data
        if letters_validator(new_href) is False:
            flash('Указано недопустимое имя для короткой ссылки')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=new_href).first():
            flash(f'Имя {new_href} уже занято!')
            return render_template('index.html', form=form)
        if form.custom_id.data is None or form.custom_id.data.strip() == '':
            form.custom_id.data = get_unique_short_id()
        obj = URLMap(
            short=form.custom_id.data,
            original=form.original_link.data,
        )
        db.session.add(obj)
        db.session.commit()
        return render_template('index.html', form=form, url=obj)
    return render_template('index.html', form=form)


@app.route('/<string:id>')
def url_view(id):
    url = URLMap.query.first_or_404(id)
    if url is not None:
        return redirect(url.original)
