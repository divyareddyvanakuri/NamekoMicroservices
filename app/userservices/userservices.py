# http_service.py
import json 
from nameko.rpc  import rpc
from models import User,authenticate_user,logout


CONFIG = {'AMQP_URI':'amqp://guecst:guest@localhost/'}

class UserServices:
    name = "userservices"

    @rpc
    def create_user(self,username,email,password):
        user = User(username,email,password)
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return json.dumps({'error':'user already registered','status':400})
        user.save(user)
        return json.dumps({'success':'user sucessfully registered','status':201})
    @rpc
    def login(self,username,password):
        return authenticate_user(username,password)
    
    
    