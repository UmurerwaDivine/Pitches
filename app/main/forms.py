from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms.fields.html5 import DateField
class PitchForm(FlaskForm):

    # Username = StringField('Username',validators=[Required()])
    description = TextAreaField('Pitches ', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
      posted = DateField('date and time')
      description = TextAreaField('your comment ', validators=[Required()])
      submit = SubmitField('Submit')
   