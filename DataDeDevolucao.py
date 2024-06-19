from datetime import datetime, timedelta


def estimar_data_devolucao(data_emprestimo):

    dia, mes, ano = map(int, data_emprestimo.split("-"))

    mes += 1
    if mes > 12:
        mes = 1
        ano += 1

    while True:
        try:
            nova_data = datetime(ano, mes, dia)
            break
        except ValueError:
            dia -= 1
    data_emprestimo = nova_data.strftime("%d-%m-%Y")
    return data_emprestimo

