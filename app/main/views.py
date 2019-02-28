from flask import render_template,request,redirect,url_for,abort
from . import main

from .forms import PitchForm,UpdateProfile,CommentForm
from .. import db
from ..models import User,Pitch,Comment
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
    pitches = Pitch.get_pitches()
    # Getting popular movie
    comments = Comment.get_comments()
    title = 'Home - Welcome to The best Pitches Review Website Online'

    return render_template('index.html', title = title, pitches=pitches,comments= comments)


@main.route('/pitch/new',methods= ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        description = form.description.data
        category = form.category.data

        # Updated review instance
        new_pitch = Pitch(description=description,category=category,user_id=current_user.id)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index',description=description,category=category ))

 
    return render_template('new_pitch.html', pitch_form=form)
@main.route('/pitch')
def show_pitch():
 pitches = Pitch.get_pitches()
 print(pitches)
 return render_template('new_pitch.html', pitches=pitches)
@main.route('/comment/new',methods= ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()
    if form.validate_on_submit():
        description = form.description.data
        posted = form.posted.data
        

        # Updated review instance
        new_comment = Comment(description=description,posted=posted,user_id=current_user.id)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.index',description=description,posted=posted ))

 
    return render_template('new_comment.html', comment_form=form)
@main.route('/comment',methods= ['GET','POST'])
def show_comment():
 comments = Comment.query.filter_by(pitch_id = id).first()
 
 comments = Comment.get_comments()
 print(comments)
 return render_template('comments.html', comments=comments)
   
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