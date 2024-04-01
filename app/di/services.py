

from fast_di import FastDIStub, DependencyCollector, FastDI
from app.repositories import (
    abstractions as abs, 
    sqlalchemy as sa_reps
)
from app import services


services_collector = DependencyCollector()

@services_collector.factory(services.ContractsService)
def provide_contracts_service(
    uow: FastDI[abs.UnitOfWork],
    contracts_repository: FastDI[abs.ContractsRepository]
) -> services.ContractsService:
    return services.ContractsService(
        uow=uow,
        contracts_repository=contracts_repository
    )