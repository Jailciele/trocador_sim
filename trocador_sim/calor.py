from pydantic import validate_arguments
from .base import BaseConversor


class CoeficienteTransferenciaCalorArgs(BaseConversor):
    escoamento_tubo: float
    pr: float


@validate_arguments
def coeficiente_transferencia_calor(args: CoeficienteTransferenciaCalorArgs) -> float:
    return 0.023 * args.escoamento_tubo ** (4 / 5) * args.pr**0.4
