from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    # Username = StringField('Username',validators=[Required()])
    description = TextAreaField('Pitches ', validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
   