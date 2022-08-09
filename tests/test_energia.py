from trocador_sim.energia import BalancoEnergiaGlobal, BalancoEnergiaGlobalArgs, Q_


def test_calculo_balanco_energia():
    args = BalancoEnergiaGlobalArgs(
        m=0.1,
        cp=2131,
        temperatura_entrada=100,
        temperatura_saida=60,
    )

    calc = BalancoEnergiaGlobal(args)
    assert calc.q == Q_(8524, "W")


def test_temperatura_saida():
    args = BalancoEnergiaGlobalArgs(
        q=8524,
        m=0.2,
        cp=4178,
        temperatura_entrada=30,
    )

    calc = BalancoEnergiaGlobal(args)
    assert round(calc.temperatura_saida, 1) == Q_(40.2, "degC")
