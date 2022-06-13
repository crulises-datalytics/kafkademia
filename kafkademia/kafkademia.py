__version__="0.1"

import argparse
from .productor import Productor
from .consumidor import Consumidor
from .utils import validar_args

def init(
    topico:str,
    bootstrap_servers:str,
    n:int,
    ej:str,
    productor_consumidor:str 
) -> None:
    validar_args(topico, bootstrap_servers, n, ej, productor_consumidor)

    if productor_consumidor == "productor":
        p = Productor(bootstrap_servers=bootstrap_servers, topico=topico)
        p.producir(ejemplo=ej, cant_mensajes=n, delay=True)
    if productor_consumidor == "consumidor":
        c = Consumidor(bootstrap_servers=bootstrap_servers, topico=topico)
        c.consumir()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topico", type=str)
    parser.add_argument("--bootstrap_servers", type=str)
    parser.add_argument("--n", type=int)
    parser.add_argument("--ej", type=str)
    parser.add_argument("--productor_consumidor", type=str)
    args = vars(parser.parse_args())

    init(**args)