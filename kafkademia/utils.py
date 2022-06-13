def validar_args(topico, bootstrap_servers, n, ej, productor_consumidor):
    assert topico is not None
    assert isinstance(topico, str)
    assert bootstrap_servers is not None
    assert isinstance(bootstrap_servers, str)
    assert isinstance(n, int)
    assert ej in ["sensor", "atm"]
    assert productor_consumidor in ["productor", "consumidor"]

    if productor_consumidor == "productor":
        assert n is not None
        assert ej is not None
