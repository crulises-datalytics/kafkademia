import argparse
from .kafkademia import main

parser = argparse.ArgumentParser()
parser.add_argument("--topico", type=str)
parser.add_argument("--bootstrap_servers", type=str)
parser.add_argument("--n", type=int)
parser.add_argument("--ej", type=str)
parser.add_argument("--productor_consumidor", type=str)
args = vars(parser.parse_args())

main(**args)