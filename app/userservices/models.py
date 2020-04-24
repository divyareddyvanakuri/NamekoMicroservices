import json
from sqlalchemy import Table, Column, Integer, String, Boolean,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import mapper,relationship,backref
from database import metadata, db_session 
import jwt
from itsdangerous import URLSafeSerializer


class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def save(self,user):
        db_session.add(user)
        db_session.commit()
        db_session.remove()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), unique=True),
    Column('email', String(120), unique=True),
    Column('password', String),
)

mapper(User, users)

def authenticate_user(username,password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return json.dumps({'error':'unauthenticated user','status_code':400})
    if user.password == password:
        auth_s = URLSafeSerializer("secret key")
        token = auth_s.dumps({'id':user.id, "username": username})
        print(token)
        return json.dumps({'token':token,'status_code':200})
    return json.dumps({'error':'unauthorized user','status_code':401})

