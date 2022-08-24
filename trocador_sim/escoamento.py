import math
from pydantic import validator, validate_arguments
from .constantes import Q_, Unit
from .base import BaseConversor


class ReynoldsArgs(BaseConversor):
    massa_especifica: Unit
    diametro: Unit
    viscosidade_dinamica: Unit

    @validator("massa_especifica")
    def conversor_massa_especifica(cls, value) -> Q_:
        return Q_(value, "kg/s")

    @validator("diametro")
    def conversor_diametro(cls, value) -> Q_:
        return Q_(value, "m")

    @validator("viscosidade_dinamica")
    def conversor_viscosidade_dinamica(cls, value) -> Q_:
        return Q_(value, "N*s/m²")


@validate_arguments
def reynolds(args: ReynoldsArgs) -> Q_:
    numerador = 4 * args.massa_especifica
    denominador = math.pi * args.diametro * args.viscosidade_dinamica
    resultado = numerador / denominador

    return resultado
