from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from src.database.models import *

UserRouter = AuthRouter[Users]("Users", Resolver[Users]())
RequestsRouter = Router[Requests]("Requests", Resolver[Requests]())

routers = (UserRouter.router, RequestsRouter.router)
