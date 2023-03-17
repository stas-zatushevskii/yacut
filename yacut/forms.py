from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from .models import URLMap


class URLForm(FlaskForm):
    original_link = StringField(
        'Введите вашу ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 512)]
    )
    custom_id = StringField(
        'Введите новую ссылку',
        validators=[Length(0, 16), Optional()]
    )
    submit = SubmitField('Создать')
