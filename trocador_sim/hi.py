from pydantic import validate_arguments, validator
from .base import BaseConversor
from .constantes import Q_, Unit


class HiArgs(BaseConversor):
    coeficiente_transferencia_calor: float
    k: Unit
    diametro: Unit

    @validator("k")
    def conversor_k(cls, value) -> Q_:
        return Q_(value, "W/(m*degK)")

    @validator("diametro")
    def conversor_diametro(cls, value) -> Q_:
        return Q_(value, "m")


@validate_arguments
def hi(args: HiArgs) -> Q_:
    return args.coeficiente_transferencia_calor * args.k / args.diametro
