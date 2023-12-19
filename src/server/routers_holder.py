from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from src.database.models import *

UserRouter = AuthRouter("Users", Users)
RequestsRouter = Router("Requests", Requests)
AnimalsRouter = Router("Animals", Animals)
DiseasesRouter = Router("Diseases", Diseases)

routers = (UserRouter.router, RequestsRouter.router, AnimalsRouter.router, DiseasesRouter.router)
