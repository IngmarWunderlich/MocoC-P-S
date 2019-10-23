from .base import MWRAPResponse

class ErrorResponse(MWRAPResponse):

    @property
    def is_recoverable(self):
        return False

    @property
    def data(self):
        pass
    
    def __init__(self, response):
        super(MWRAPResponse,response).__init()