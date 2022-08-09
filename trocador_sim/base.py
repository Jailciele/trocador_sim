from pydantic import BaseModel, root_validator


class BaseConversor(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True

    @root_validator
    def grau_de_liberdade(cls, values: dict) -> dict:
        if list(values.values()).count(None) > 1:
            raise ValueError("Deve haver apenas uma icognita.")
        return values
