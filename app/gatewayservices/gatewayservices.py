# http_service.py
import json 
from nameko.web.handlers import http

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class HttpRegistrationService:
    name = "gatewayservices"
    
   
    @http('GET', '/get')
    def get_method(self, request):
        return "welcome to Services"

    @http('POST', '/register')
    def register(self, request):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        

    @http('POST', '/login')
    def login(self, request):
        username = request.form['username']
        password = request.form['password']

    
    @http('POST', '/create')
    def post_method(self, request):
        title = request.form['title']
        text = request.form['text']
        archive = request.form['archive']
        color = request.form['color']
        
    
    @http('PUT', '/edit/<int:id>')      
    def put_method(self,request,id):
        title = request.form['title']
        text = request.form['text']
        archive = request.form['archive']
        color = request.form['color']
       
    
    @http('DELETE', '/delete/<int:id>') 
    def delete_method(self,request,id):
        pass