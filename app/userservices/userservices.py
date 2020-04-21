# http_service.py
import json 
from nameko.rpc  import rpc


CONFIG = {'AMQP_URI':'amqp://guecst:guest@localhost/'}

class UserServices:
    name = "userservices"

    @rpc
    def create_user(self,username,email,password):
        return "successfully registered"

    @rpc
    def login(self,username,password):
        return "successfully logged in"
    