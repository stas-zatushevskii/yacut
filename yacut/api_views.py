from flask import jsonify, request, url_for

from . import app, db
from .models import URLMap
from .validators import letters_validator
from .views import get_unique_short_id
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_new_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()

    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    result = url.to_dict()
    return jsonify(
        {
            'url': result['original']
        }), 200


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' in data:
        new_url = data['custom_id']
        if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage(f'Имя "{new_url}" уже занято.')
    if (
        'custom_id' not in data or data['custom_id'] is None or data['custom_id'].strip() == ''
    ):
        data['custom_id'] = get_unique_short_id()
    if letters_validator(data['custom_id']) is False:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    data = request.get_json()
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    result = url.to_dict()
    return jsonify(
        {
            'url': result["original"], 'short_link': url_for('url_view', id=data['custom_id'], _external=True)
        }
    ), 201
