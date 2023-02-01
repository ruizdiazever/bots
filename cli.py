import argparse
from src.core.moon.app import start_moon
from src.core.xtx.app import start_xtx


parser = argparse.ArgumentParser(prog = 'cli.py',
                    description = 'Minibots to help in everything!',
                    epilog = 'Write python cli.py -h')


parser.add_argument('--moon', metavar='', dest="moon", type=int, help='Cripto boot, to the moon!')
parser.add_argument('--xtx', metavar='', dest="xtx", type=int, help='Ant to search stock :D')


args = parser.parse_args()
print(args)

#start_moon()
