from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length


message = "Este campo não pode ficar em branco."


class RateMovieForm(FlaskForm):
    new_rating = FloatField(
        label="Your rating out of 10 e.g. 7.5",
        validators=[DataRequired(message=message), NumberRange(min=0, max=10)]
    )
    new_review = StringField(
        label="Your review",
        validators=[DataRequired(message=message), Length(min=1, max=250)]
    )
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired(message=message)])
    submit = SubmitField("Add Movie")
