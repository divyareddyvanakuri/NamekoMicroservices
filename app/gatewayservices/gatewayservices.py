# http_service.py
import json 
from werkzeug.wrappers import Response
from nameko.web.handlers import http
from nameko.standalone.rpc import ClusterRpcProxy
from nameko.rpc import RpcProxy
from itsdangerous import URLSafeSerializer,BadSignature


config = {'AMQP_URI':'amqp://guest:guest@localhost/'}


class HttpGatewayServices:
    name = "gatewayservices"
    
    userservices = RpcProxy('userservices')
    noteservices = RpcProxy('noteservices')
    
    
    @http('GET', '/get')
    def get_method(self, request):
        return "welcome to Services"

    @http('POST', '/register')
    def register(self, request):
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirmpassword = request.form['confirmpassword']
        except (KeyError,AttributeError,TypeError):
            return Response(json.dumps({"error":"Invalide key names","status_code":400}))
        if password == confirmpassword:
            with ClusterRpcProxy(config) as rabbit:
                return Response(rabbit.userservices.create_user(username,email,password))
        return Response(json.dumps({"error":"password mismatch","status_code":400}))
    

    @http('POST', '/login')
    def login(self, request):
        try:
            username = request.form['username']
            password = request.form['password']
        except (KeyError,AttributeError,TypeError):
            return Response(json.dumps({"error":"Invalide Key names","status_code":400}))
        print(request.form)
        with ClusterRpcProxy(config) as rabbit:
            return Response(rabbit.userservices.login(username,password))
    
    @http('POST', '/create')
    def post_method(self, request):
        try:
            token = request.headers['token']
            userid = authorization(token)
        except (KeyError,BadSignature) as err:
            return Response(json.dumps({"error":"something went wrong,please login again","status_code":400}))
        try:
            title = request.form['title']
            text = request.form['text']
            archive = request.form['archive']
            color = request.form['color']
        except (KeyError,AttributeError,TypeError):
            return Response(json.dumps({"error":"Invalide key names","status_code":400}))
        with ClusterRpcProxy(config) as rabbit:
            return Response(rabbit.noteservices.create_note(userid,title,text,archive,color))
    
    @http('PUT', '/edit/<int:id>')      
    def put_method(self,request,id):
        try:
            token = request.headers['token']
            userid = authorization(token)
        except (KeyError,BadSignature) as err:
            return Response(json.dumps({"error":"something went wrong,please login again","status_code":400}))
        try:
            title = request.form['title']
            text = request.form['text']
            archive = request.form['archive']
            color = request.form['color']
        except (KeyError,AttributeError,TypeError):
            return Response(json.dumps({"error":"Invalide key names","status_code":400}))
        with ClusterRpcProxy(config) as rabbit:
            return Response(rabbit.noteservices.edit_note(id,userid,title,text,archive,color))
    
    @http('DELETE', '/delete/<int:id>') 
    def delete_method(self,request,id):
        try:
            token = request.headers['token']
            userid = authorization(token)
        except (KeyError) as err:
            return Response(json.dumps({"error":"something went wrong,please login again","status_code":400}))
        
        with ClusterRpcProxy(config) as rabbit:
            return Response(rabbit.noteservices.delete_note(id,userid))
    
    
def authorization(token):
    print(token)
    auth_s = URLSafeSerializer("secret key")
    user = auth_s.loads(token)
    print(user)
    userid = user['id']
    return userid
    