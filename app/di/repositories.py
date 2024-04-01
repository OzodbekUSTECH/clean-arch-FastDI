from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from fast_di import FastDIStub, DependencyCollector
from app.repositories import abstractions
from app.repositories import sqlalchemy as sa_reps


reps_collector = DependencyCollector()


@reps_collector.factory(abstractions.UnitOfWork)
def provide_uow(session: FastDIStub[AsyncSession]) -> abstractions.UnitOfWork:
    return sa_reps.SqlalchemyUnitOfWork(session)


@reps_collector.factory(abstractions.ContractsRepository)
def provide_contracts_repository(
    session: FastDIStub[AsyncSession],
) -> abstractions.ContractsRepository:
    return sa_reps.SqlalchemyContractsRepository(session)
