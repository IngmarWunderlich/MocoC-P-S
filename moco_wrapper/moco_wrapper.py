# -*- coding: utf-8 -*-

from . import models
from . import util
from requests import get, post, put, delete
from json import dumps
from .const import API_PATH

"""Main module."""
class Moco(object):
    """The Moco class provides access to moco's api

    .. code-block:: python

    import moco_wrapper
    moco = moco_wrapper.Moco(email='EMAIL_ADDRESS', password='PASSWORD', api_key='API_KEY', domain='DOMAIN')

    """
    def __init__(self, api_key = None, domain = None):
        self.api_key = api_key
        self.domain = domain

        #init contacts model

        self.Contact = models.Contact(self)
        self.Company = models.Company(self)
        self.Comment = models.Comment(self)
        self.Unit = models.Unit(self)

        self.User = models.User(self)
        self.Schedule = models.Schedule(self)

        self.Project = models.Project(self)
        self.ProjectContract = models.ProjectContract(self)
        self.ProjectExpense = models.ProjectExpense(self)

        self.requester = util.RateLimiter()

    def request(self, method, path, params=None, data=None):
        full_path = self.full_domain + path
        """Send a request to an URL with the specified params and data"""
        if method == "GET":
            return self.requester.get(full_path, params=params, data=data, headers=self.headers)
        elif method == "PUT":
            return self.requester.put(full_path, params=params, data=data, headers=self.headers)
        elif method == "POST":
            return self.requester.post(full_path, params=params, data=data, headers=self.headers)
        elif method == "DELETE":
            return self.requester.delete(full_path, params=params, data=data, headers=self.headers)
        
    def get(self, path, params=None, data=None):
        return self.request("GET", path, params=params, data=data)
        
    def post(self, path, params=None, data=None):
        return self.request("POST", path, params=params, data=data)

    def put(self, path, params=None, data=None):
        return self.request("PUT", path, params=params, data=data)

    def delete(self, path, params=None, data=None):
        return self.request("DELETE", path, params=params, data=data)

    @property
    def headers(self):
        headers = {
            'Content-Type' : 'application/json',
            'Authorization': 'Token token={}'.format(self.api_key)
        }
        return headers

    @property
    def full_domain(self):
        return "https://{}.mocoapp.com/api/v1".format(self.domain)

    
    
