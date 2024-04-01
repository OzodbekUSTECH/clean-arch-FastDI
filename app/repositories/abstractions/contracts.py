from uuid import UUID
from typing import Protocol

from app import models
from app.schemes import contracts as contract_schemes


class ContractsRepository(Protocol):

    async def create_contract(
        self, contract_data: contract_schemes.CreateContractSchema
    ) -> models.Contract:
        raise NotImplementedError
    
    async def get_contracts(self) -> list[models.Contract]:
        raise NotImplementedError

    async def get_contract(self, id: UUID) -> models.Contract | None:
        raise NotImplementedError

    
