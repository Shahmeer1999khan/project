import logging

logger = logging.getLogger(__name__)


class RequestLoggerMiddleware:
    
    def __init__(self, get_respone):
        self.get_response = get_respone
        
    def __call__(self,request):
        logger.info(f"Incoming request: {request.method} {request.path}")
        
        response = self.get_response(request)
        
        logger.info(f"Outing response: {response.status_code}")
        
        return response
    