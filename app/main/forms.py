from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateTimeField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    # Username = StringField('Username',validators=[Required()])
    description = TextAreaField('Pitches ', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
      posted = DateTimeField('date and time',format='%Y-%m-%d %H:%M:%S', validators = [Required()])
      description = TextAreaField('your comment ', validators=[Required()])
      submit = SubmitField('Submit')
   