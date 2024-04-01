from app.di.db import db_collector
from app.di.repositories import reps_collector
from app.di.services import services_collector

all_dependencies = [
    db_collector,
    reps_collector,
    services_collector
]