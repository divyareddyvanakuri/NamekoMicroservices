# http_service.py
import json 
from nameko.web.handlers import http
from nameko.standalone.rpc import ClusterRpcProxy
from nameko.rpc import RpcProxy

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class HttpRegistrationService:
    name = "gatewayservices"
    
    userservices = RpcProxy('userservices')
    noteservices = RpcProxy('noteservices')
    
    @http('GET', '/get')
    def get_method(self, request):
        return "welcome to Services"

    @http('POST', '/register')
    def register(self, request):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        if password == confirmpassword:
            with ClusterRpcProxy(config) as rabbit:
                return 201,json.dumps({'success': rabbit.userservices.create_user(username,email,password)})
        return 404,json.dumps({'error':'password mismatch'})
    

    @http('POST', '/login')
    def login(self, request):
        username = request.form['username']
        password = request.form['password']
        with ClusterRpcProxy(config) as rabbit:
            return 200,json.dumps({'sucsess':rabbit.userservices.login(username,password)})
    
    @http('POST', '/create')
    def post_method(self, request):
        title = request.form['title']
        text = request.form['text']
        archive = request.form['archive']
        color = request.form['color']
        with ClusterRpcProxy(config) as rabbit:
            return 201,json.dumps({'sucsess':rabbit.noteservices.create_note(title,text,archive,color)})
    
    @http('PUT', '/edit/<int:id>')      
    def put_method(self,request,id):
        title = request.form['title']
        text = request.form['text']
        archive = request.form['archive']
        color = request.form['color']
        with ClusterRpcProxy(config) as rabbit:
            return 200,json.dumps({'sucsess':rabbit.noteservices.edit_note(id,title,text,archive,color)})
    
    @http('DELETE', '/delete/<int:id>') 
    def delete_method(self,request,id):
        pass