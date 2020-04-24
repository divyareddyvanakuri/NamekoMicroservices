from sqlalchemy import Table, Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import mapper,relationship,backref
from database import metadata, db_session 
from itsdangerous import URLSafeSerializer

class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
        
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), unique=True),
    Column('email', String(120), unique=True),
    Column('password', String),
)

mapper(User, users)

class Note(object):
    query = db_session.query_property()

    def __init__(self, title=None, text=None, archive=None, color=None, userid=None):
        self.title = title
        self.text = text
        self.archive = archive
        self.color = color
        self.userid = userid

    def __repr__(self):
        return '<Note %r>' % (self.title)

    def save(self,note):
        db_session.add(note)
        db_session.commit()
        db_session.remove()
    
    def delete(self,note):
        db_session.delete(note)
        db_session.commit()
        db_session.remove()
    
    def update(self):
        db_session.commit()
        db_session.remove()

notes = Table('notes', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('text', String),
    Column('color', String),
    Column('archive',Boolean,default=False,nullable=False),
    Column('userid',Integer,ForeignKey("users.id"),nullable=False),
)

mapper(Note,notes)
