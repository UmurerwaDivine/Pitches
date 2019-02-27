from flask import render_template,request,redirect,url_for,abort
from . import main

from .forms import PitchForm,UpdateProfile
from .. import db
from ..models import User,Pitch
from flask_login import login_required,current_user
from .. import db,photos


# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     message = 'Hello World'
#     return render_template('index.html',message = message)
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie

    title = 'Home - Welcome to The best Pitches Review Website Online'

    return render_template('index.html', title = title)


@main.route('/user/<uname>',methods= ['POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    if form.validate_on_submit():
        description = form.description.data
        pitch = form.pitch.data

        # Updated review instance
        new_pitch = Pitch(pitch_id=pitch.id,description=description,user=current_user)

        # save review method
        return new_pitch.save_pitch()
        #  redirect(url_for('.pitch',id = pitch.id ))

 
    return render_template('new_pitch.html', pitch_form=form)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))