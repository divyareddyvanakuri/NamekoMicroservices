# http_service.py
import json 
from nameko.rpc  import rpc
from models import User

CONFIG = {'AMQP_URI':'amqp://guecst:guest@localhost/'}

class UserServices:
    name = "userservices"

    @rpc
    def create_user(self,username,email,password):
        user = User(username,email,password)
        user.save(user)
        return "successfully registered"

    @rpc
    def login(self,username,password):
       return "successfully logged in"
    