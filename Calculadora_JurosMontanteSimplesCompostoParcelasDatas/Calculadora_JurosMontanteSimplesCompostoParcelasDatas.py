"""
instalar:
pip install python-dateutil types-python-dateutil
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

while True:
    ano = input('Em que ano foi pedido o empréstimo? ').strip()
    mes = input('Em que mês foi pedido o empréstimo [1 - 12]? ').strip()
    dia = input('Em que dia foi pedido o empréstimo? ').strip()
    if ano.isdigit() and mes.isdigit() and dia.isdigit():
        ano, mes, dia = int(ano), int(mes), int(dia)
    else:
        print('Atenção, ano, mês e dia devem ser números inteiros!!!')
        continue

    data_emprestimo = datetime(ano, mes, dia)
    data_parcelas = []
    data_parcela = data_emprestimo

    capital = input("\nQual o valor desejado/emprestado? R$").replace(',','.').strip()
    if capital.replace('.', '').isdigit():
        capital = float(capital)
    else:
        print('Atenção, o capital deve ser um valor válido [números, ponto ou vírgula]!!!')
        continue

    tipo_tempo = input('\npagar uma parcela por ano [1] '
                        '\npagar uma parcela por mês [2] '
                        '\npagar uma parcela por dia [3]'
                        '\nSelecione uma das opções acima: ')

    if tipo_tempo!='1' and tipo_tempo!='2' and tipo_tempo!='3':
        print('Atenção, para selecionar o tipo de parcelamento selecione apenas uma das opções na lista [1] [2] ou [3]')
        continue

    if tipo_tempo == '1':
        tempo = input("Quantos anos de empréstimo? ").strip()
        if tempo.isdigit():
            tempo = int(tempo)
        else:
            print('Atenção ano deve ser um número inteiro!!!')
            continue
        delta_anos = relativedelta(years=tempo)
        data_final = data_emprestimo + delta_anos
    elif tipo_tempo == '2':
        tempo = input("Quantos meses de empréstimo? ").strip()
        if tempo.isdigit():
            tempo = int(tempo)
        else:
            print('Atenção mês deve ser um número inteiro!!!')
            continue
        delta_meses = relativedelta(months=tempo)
        data_final = data_emprestimo + delta_meses
    else:
        tempo = input("Quantos dias de empréstimo? ").strip()
        if tempo.isdigit():
            tempo = int(tempo)
        else:
            print('Atenção dia deve ser um número inteiro!!!')
            continue
        delta_dias = relativedelta(days=tempo)
        data_final = data_emprestimo + delta_dias

    tipo_juros = input("\njuros simples [1] ou juros composto [2]? ").strip()

    if tipo_juros != '1' and tipo_juros != '2':
        print('Atenção, para selecionar o tipo de juros selecione apenas uma das opções na lista [1] ou [2]')
        continue

    juros = input("Qual a taxa de juros [exemplo: 0.1 equivale a 10%]? ").replace(',','.')

    if juros.replace('.','').isdigit():
            juros = float(juros)
    else:
        print('Atenção, o juros deve ser um valor válido [números, ponto ou vírgula]!!!')
        continue

    taxa = juros
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

    print('')
    numero_parcelas = len(data_parcelas)
    capital_inicial = capital
    for data in data_parcelas:
        if tipo_juros=='1':
            valor_parcela = montante/numero_parcelas
            print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')
        else:
            valor_parcela = (capital*taxa)
            capital = capital+valor_parcela
            print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela+(capital_inicial/numero_parcelas):,.2f}')
        

    print()

    if tipo_tempo=='1':
        print(
            f'\nVocê pegou R$ {capital_inicial:,.2f} para pagar '
            f'em {tempo} anos \n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
    elif tipo_tempo=='2':
        print(
            f'\nVocê pegou R$ {capital_inicial:,.2f} para pagar '
            f'em {tempo} meses \n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
    else:
        print(
            f'\nVocê pegou R$ {capital_inicial:,.2f} para pagar '
            f'em {tempo} dias \n'
            f'O montante total foi de R${montante:.2f}\n'
            f'O juros em reais foi de R${juros:.2f}'
        )
        
    print('')
    print('-'*100)
    print('')


    sair = input('Deseja sair do app? [s]im [n]ão: ').strip().lower()
    if sair == 's': break