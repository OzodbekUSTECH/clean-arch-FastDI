from fastapi import APIRouter
from app.schemes import contracts as contract_schemes
from app.services import ContractsService
from fast_di import FastDIStub
from uuid import UUID


router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)

@router.post('/')
async def create_contract(
    contracts_service: FastDIStub[ContractsService],
    contract_data: contract_schemes.CreateContractSchema
) -> contract_schemes.ContractSchema:
    return await contracts_service.create_contract(contract_data=contract_data)

@router.get('/')
async def get_contracts(
    contracts_service: FastDIStub[ContractsService]
) -> list[contract_schemes.ContractSchema]:
    return await contracts_service.get_contracts()

@router.get('/{id}')
async def get_contract_by_id(
    contracts_service: FastDIStub[ContractsService],
    id: UUID
) -> contract_schemes.ContractSchema:
    return await contracts_service.get_contract(id=id)