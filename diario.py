import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

    # Tratando dias em que o faturamento é zero (finais de semana e feriados)
    dados = [aux for aux in dados if aux['faturamento_diario'] != 0]


menor = min(aux['faturamento_diario'] for aux in dados)
maior = max(aux['faturamento_diario'] for aux in dados)

faturamento_mensal = sum([aux['faturamento_diario'] for aux in dados])
media = faturamento_mensal/len(dados)

acima_media = [aux['faturamento_diario'] for aux in dados if aux['faturamento_diario'] > media]


print("MENOR valor faturado no mês:", menor)
print("MAIOR valor faturado no mês:", maior)
print("Número de dias em que o faturamento diário foi superior à média mensal:", len(acima_media))

