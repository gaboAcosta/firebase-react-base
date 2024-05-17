import importlib
import os

from fastapi import APIRouter, Depends
from fastapi.security import APIKeyCookie

from api.dependencies.auth import validate_cookie_session

base_router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

public_routes_dir = 'routes/public'
private_routes_dir = 'routes/private'


def load_routes(router: APIRouter, routes_dir: str) -> APIRouter:
    root_dir = os.path.dirname(__file__)
    path = f'{root_dir}/{routes_dir}'
    files = os.listdir(path)
    python_files = [file for file in files if file.endswith('.py')]
    for file in python_files:
        module_name = file[:-3]  # Remove the .py extension
        full_module_name = f'api/{routes_dir}/{module_name}'.replace('/', '.')
        route_module = importlib.import_module(full_module_name)
        if not route_module or not route_module.router:
            raise Exception(f"Error loading app routes, Module {full_module_name} does not have a router")
        router.include_router(route_module.router)

    return router


def load_public_router() -> APIRouter:
    router = APIRouter(
        prefix="/v1",
    )
    return load_routes(router, public_routes_dir)


def load_private_router() -> APIRouter:
    cookie_scheme = APIKeyCookie(name="__session")
    router = APIRouter(
        prefix="/v1",
        dependencies=[Depends(validate_cookie_session), Depends(cookie_scheme)],
    )
    return load_routes(router, private_routes_dir)


base_router.include_router(load_public_router())
base_router.include_router(load_private_router())
