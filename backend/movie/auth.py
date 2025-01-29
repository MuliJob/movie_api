"""Authentication keyword"""
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthentication(BaseTokenAuth):
    """Setting the bearer key word"""
    keyword = 'Bearer'