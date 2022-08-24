from trocador_sim.escoamento import ReynoldsArgs, reynolds, Q_


def test_reynolds():
    args = ReynoldsArgs(
        massa_especifica=0.2,
        diametro=0.025,
        viscosidade_dinamica=725e-6,
    )

    resultado = reynolds(args)

    assert round(resultado, 0) == 14_050


def test_reynolds_anular():
    args = ReynoldsArgs(
        massa_especifica=0.1,
        diametro=(0.045 + 0.025),
        viscosidade_dinamica=Q_(3.25e-2, "kg/(s*m)"),
    )

    resultado = reynolds(args)

    assert round(resultado, 0) == 56
