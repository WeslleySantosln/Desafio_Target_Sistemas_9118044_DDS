"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""

import json


acima_da_media = 0

with open("arquivos/dados.json", "r") as arquivo:
    dados = json.load(arquivo)

valores_validos = []



for item in dados:
    if item["valor"] > 0:
        valores_validos.append(item["valor"])


menor = min(valores_validos)
maior = max(valores_validos)


media = sum(valores_validos) / len(valores_validos)

for item in dados:
    if item["valor"] > media:
        acima_da_media += 1 


print(f"O menor faturamento do mês foi: R$ {menor}")
print(f"O maior faturamento do mês foi: R$ {maior}")
print(f"Os dias com faturamento acima da média foram: {acima_da_media}")
