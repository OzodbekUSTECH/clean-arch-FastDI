from fastapi import FastAPI
from app.api import all_routers
from app.di import all_dependencies
from app.config import settings
from fast_di import init_dependencies

app = FastAPI(
    title="CLEAN ARCHITECTURE FAST DI"
)

for router in all_routers:
    app.include_router(router, prefix=settings.api_prefix)

init_dependencies(app, *all_dependencies)


