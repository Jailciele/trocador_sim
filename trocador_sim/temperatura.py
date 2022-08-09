import math
from pydantic import validator, validate_arguments
from .constantes import Q_, Unit
from .base import BaseConversor


class DeltaTmlArgs(BaseConversor):
    entrada_quente: Unit
    saida_quente: Unit
    entrada_frio: Unit
    saida_frio: Unit

    @validator("*")
    def conversor_temperatura(cls, value) -> Q_:
        return Q_(value, "degC")


@validate_arguments
def delta_t_ml(args: DeltaTmlArgs) -> Q_:
    numerador = (args.entrada_quente - args.saida_frio) - (
        args.saida_quente - args.entrada_frio
    )
    denominador = math.log(
        (args.entrada_quente - args.saida_frio)
        / (args.saida_quente - args.entrada_frio)
    )
    resultado = numerador / denominador

    return Q_(resultado.magnitude, "degC")
