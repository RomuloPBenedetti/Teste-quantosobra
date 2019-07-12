
import argparse
import textwrap
import sys


def reorder(start, end, cars_numb):
    """
    Reordena a lista da partida da corrida via pop inserts a partir da esquerda tendo a
    lista de chegada como sequência esperada, contabilizando o deslocamento de índices
    para descobrir o número mínimo de ultrapassagens.

    :param start: lista a ser ordenada.
    :param end: lista na ordem esperada.
    :param cars_numb: número de carros
    :return: Número mínimo de ultrapassagens.
    """
    overtaking_count = 0

    for a in range(cars_numb):
        for b in range(a, cars_numb):
            if end[a] == start[b]:
                overtaking_count += b - a
                start.insert(a, start.pop(b))

    return overtaking_count


def gen_parser():
    s = textwrap.dedent('''
    Descrição:
        Calcula o número mínimo de ultrapassagens em uma corrida de carros.
                        ''')
    e = textwrap.dedent('''
    Exemplos de uso: 
        python t4.py -n 4 -p 1 2 3 4 -c 3 4 2 1  
                        ''')
    parser = argparse.ArgumentParser(prog='QuantoSobra_ultrapassagem',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=s, epilog=e)
    s = "Ordem de partida dos carros."
    parser.add_argument("-p", "--partida", type=int, help=s, nargs='*')
    s = "Ordem de chegada dos carros."
    parser.add_argument("-c", "--chegada", type=int, help=s, nargs='*')
    s = "Número de carros na corrida."
    parser.add_argument("-nc", "--num-de-carros", type=int, help=s)
    return parser


def execute():

    if len(args.partida) != args.num_de_carros:
        parser.error("Ops! Algum carro está faltando ou sobrando na partida!.")

    if len(args.chegada) != args.num_de_carros:
        parser.error("Ops! Algum carro está faltando ou sobrando na chegada!.")

    if set(args.partida) != set(args.chegada):
        parser.error("Ops! Algum carro trocou de número!.")

    if args.num_de_carros == 0:
        print("0 ultrapassagens")
        exit()

    overtaking_count = reorder(args.partida, args.chegada, args.num_de_carros)
    print("%s ultrapassagens" % overtaking_count)


if __name__ == '__main__':
    parser = gen_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("Nenhum argumento encontrado.")

    execute()
