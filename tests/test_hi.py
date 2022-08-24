from trocador_sim.hi import HiArgs, hi, Q_


def test_hi():
    args = HiArgs(
        coeficiente_transferencia_calor=90,
        k=0.625,
        diametro=0.025,
    )

    resultado = hi(args)
    assert round(resultado, 0) == Q_(2250, "W/(m²*degK)")
