from datetime import datetime
from dateutil.relativedelta import relativedelta

#valor total do empréstimo
valor_total = float(input("Qual o valor total?"))

#data do empréstimo
ano = int(input('Qual o ano?'))
mes = int(input('Qual o mês? [1 - 12]'))
dia = int(input('Qual o dia?'))
data_emprestimo = datetime(ano, mes, dia)

#tempo de duração do empréstimo
tipo_duracao = input("O empréstimo é em anos [1], meses [2] ou dias [3]: ").strip()
if tipo_duracao=='1':
    duracao = int(input("Quantos anos de empréstimo?"))
    delta_anos = relativedelta(years=duracao)
    data_final = data_emprestimo + delta_anos
elif tipo_duracao=='2':
    duracao = int(input("Quantos meses de empréstimo?"))
    delta_meses = relativedelta(months=duracao)
    data_final = data_emprestimo + delta_meses
else:
    duracao = int(input("Quantos dias de empréstimo?"))
    delta_dias = relativedelta(days=duracao)
    data_final = data_emprestimo + delta_dias

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    if tipo_duracao=='1':
        data_parcela += relativedelta(months=+1)
    elif tipo_duracao=='2':
        data_parcela += relativedelta(months=+1)
    else:
        data_parcela += relativedelta(days=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas


for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()

if tipo_duracao=='1':
    print(
        f'Você pegou R$ {valor_total:,.2f} para pagar '
        f'em {delta_anos.years} anos '
        f'({numero_parcelas} meses) em parcelas de '
        f'R$ {valor_parcela:,.2f}.'
    )
elif tipo_duracao=='2':
    print(
        f'Você pegou R$ {valor_total:,.2f} para pagar '
        f'em {delta_meses.months} meses '
        f'({numero_parcelas} meses) em parcelas de '
        f'R$ {valor_parcela:,.2f}.'
    )
else:
    print(
        f'Você pegou R$ {valor_total:,.2f} para pagar '
        f'em {delta_dias.days} dias '
        f'({numero_parcelas} pacelas) em parcelas de '
        f'R$ {valor_parcela:,.2f}.'
    )
    