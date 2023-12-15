from src.server.router import Router, Resolver
from src.server.resolver import TModel
from .auth_resolver import login

class AuthRouter(Router[TModel]):
    def __init__(self, name, resolver: Resolver[TModel]):
        super(AuthRouter, self).__init__(name, resolver)
        self.router.add_api_route('/login', self.login, methods=["get"])

    def login(self, name: str, password: str):
        return login(name, password)
