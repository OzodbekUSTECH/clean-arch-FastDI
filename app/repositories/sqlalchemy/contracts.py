from app.repositories.abstractions.contracts import ContractsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from uuid import UUID
from app import models
from app.schemes import contracts as contract_schemes

class SqlalchemyContractsRepository(ContractsRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_contract(self, contract_data: contract_schemes.CreateContractSchema) -> models.Contract:
        stmt = insert(models.Contract).values(**contract_data.model_dump()).returning(models.Contract)
        result = await self.session.execute(stmt)
        return result.scalar_one()
    
    async def get_contracts(self) -> list[models.Contract]:
        stmt = select(models.Contract)
        result = await self.session.execute(stmt)
        return result.scalars().all()
    
    async def  get_contract(self, id: UUID) -> models.Contract | None:
        stmt = select(models.Contract).where(models.Contract.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()