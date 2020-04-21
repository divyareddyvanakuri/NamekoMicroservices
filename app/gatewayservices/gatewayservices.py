# http_service.py
import json 
from nameko.web.handlers import http

class HttpService:
    name = "gatewayservices"
        
    @http('GET', '/get')
    def get_method(self, request):
        return "welcome to Services"

    