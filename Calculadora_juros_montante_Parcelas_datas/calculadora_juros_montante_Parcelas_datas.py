from datetime import datetime
from dateutil.relativedelta import relativedelta

while True:
    ano = int(input('Em que ano foi pedido o empréstimo?'))
    mes = int(input('Em que mês foi pedido o empréstimo? [1 - 12]'))
    dia = int(input('Em que dia foi pedido o empréstimo?'))
    data_emprestimo = datetime(ano, mes, dia)
    data_parcelas = []
    data_parcela = data_emprestimo

    capital = float(input("Qual o valor desejado/emprestado? R$").replace(',','.'))
    tipo_tempo = input("calculo em anos [1], meses [2] ou dias [3]? ")
    if tipo_tempo == '1':
        tempo = int(input("Quantos anos de empréstimo?"))
        delta_anos = relativedelta(years=tempo)
        data_final = data_emprestimo + delta_anos
    elif tipo_tempo == '2':
        tempo = int(input("Quantos meses de empréstimo?"))
        delta_meses = relativedelta(months=tempo)
        data_final = data_emprestimo + delta_meses
    else:
        tempo = int(input("Quantos dias de empréstimo?"))
        delta_dias = relativedelta(days=tempo)
        data_final = data_emprestimo + delta_dias
    tipo_juros = input("juros simples [1] ou juros composto [2]? ")
    juros = float(input("Qual a taxa de juros [exemplo: 0.1 equivale a 10%]? ").replace(',','.'))
    if tipo_juros=='1':
        montante_simples = capital*(1+(juros*tempo))
        juros = montante_simples-capital
        montante = montante_simples
    else:
        montante_composto = capital*((1+juros)**tempo)
        juros = montante_composto-capital
        montante = montante_composto

    while data_parcela < data_final:
        data_parcelas.append(data_parcela)
        if tipo_tempo=='1':
            data_parcela += relativedelta(years=+1)
        elif tipo_tempo=='2':
            data_parcela += relativedelta(months=+1)
        else:
            data_parcela += relativedelta(days=+1)

    numero_parcelas = len(data_parcelas)
    valor_parcela = montante / numero_parcelas

    for data in data_parcelas:
        print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

    print()

    if tipo_tempo=='1':
        print(
            f'Você pegou R$ {capital:,.2f} para pagar '
            f'em {delta_anos.years} anos \n'
            f'({numero_parcelas} meses) em parcelas de '
            f'R${valor_parcela:,.2f}.\n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
    elif tipo_tempo=='2':
        print(
            f'Você pegou R$ {capital:,.2f} para pagar '
            f'em {delta_meses.months} meses \n'
            f'({numero_parcelas} meses) em parcelas de '
            f'R$ {valor_parcela:,.2f}.\n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
    else:
        print(
            f'Você pegou R$ {capital:,.2f} para pagar '
            f'em {delta_dias.days} dias \n'
            f'({numero_parcelas} pacelas) em parcelas de '
            f'R$ {valor_parcela:,.2f}.\n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
        
    print('')
    print('-'*100)
    print('')