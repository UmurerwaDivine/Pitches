from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    
    # Flask-Login integration
    def is_authenticated(self):
       return True

    def is_active(self):
       return True

    def is_anonymous(self):
       return False

    def get_id(self):
       return self.id

   
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return f'User {self.name}'
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(id):
        pitches = Pitch.query.all()
        return pitches      
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    description =db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    def __repr__(self):
        return f'User {self.name}'

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(id):
        comments = Comment.query.all()
        return comments