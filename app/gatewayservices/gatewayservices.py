# http_service.py
import json 
from nameko.web.handlers import http

config = {'AMQP_URI':'amqp://guest:guest@localhost/'}

class HttpRegistrationService:
    name = "gatewayservices"
    
    @http('GET', '/get')
    def get_method(self, request):
        return "welcome to Services"

    