from pydantic import BaseModel
from uuid import UUID

class CreateContractSchema(BaseModel):
    title: str

class UpdateContractSchema(CreateContractSchema):
    pass

class ContractSchema(UpdateContractSchema):
    id: UUID