import json

with open('dadosMensais.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento_geral = sum(aux['faturamento_mensal'] for aux in dados)

porcentagens_proporcionais = [(aux['faturamento_mensal'] / faturamento_geral) * 100 for aux in dados]

porcentagens_proporcionais_arredondadas = [round(porcentagem, 2) for porcentagem in porcentagens_proporcionais]

print(porcentagens_proporcionais_arredondadas)
