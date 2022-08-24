from trocador_sim.calor import (
    CoeficienteTransferenciaCalorArgs,
    coeficiente_transferencia_calor,
)


def test_coeficiente_transferencia_calor():
    args = CoeficienteTransferenciaCalorArgs(
        escoamento_tubo=14_050,
        pr=4.85,
    )

    resultado = coeficiente_transferencia_calor(args)
    assert round(resultado, 0) == 90
