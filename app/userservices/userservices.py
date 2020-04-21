# http_service.py
import json 
from nameko.rpc  import rpc


class UserServices:
    name = "userservices"

    @rpc
    def create_user(self,username,email,password):
        return "successfully registered"

    
    