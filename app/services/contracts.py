from app.schemes import contracts as contract_schemes
from app.repositories import abstractions as abs
from uuid import UUID


class ContractsService:

    def __init__(
            self,
            uow: abs.UnitOfWork,
            contracts_repository: abs.ContractsRepository
    ):
        self.uow = uow
        self.contracts_repo = contracts_repository

    async def create_contract(self, contract_data: contract_schemes.CreateContractSchema) -> contract_schemes.ContractSchema:
        created_contract = await self.contracts_repo.create_contract(contract_data=contract_data)
        await self.uow.commit()
        return created_contract

    async def get_contracts(self) -> list[contract_schemes.ContractSchema]:
        return await self.contracts_repo.get_contracts()
    
    async def get_contract(self, id: UUID) -> contract_schemes.ContractSchema:
        return await self.contracts_repo.get_contract(id=id)