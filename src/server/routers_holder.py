from .router import Router
from .resolver import Resolver
from src.database.models import *

UserRouter = Router[Users]("Users", Resolver[Users]())
RequestsRouter = Router[Requests]("Requests", Resolver[Requests]())

routers = (UserRouter.router, RequestsRouter.router)
