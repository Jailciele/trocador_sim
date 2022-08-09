from trocador_sim.temperatura import DeltaTmlArgs, delta_t_ml, Q_


def test_delta_t_ml():
    args = DeltaTmlArgs(
        entrada_frio=30,
        saida_frio=40.2,
        entrada_quente=100,
        saida_quente=60,
    )

    resultado = delta_t_ml(args)

    assert round(resultado, 1) == Q_(43.2, "degC")
