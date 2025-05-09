"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
"""

cidades = {}
soma = 0

cidades["SP"] = 67836.43
cidades["RJ"] = 36678.66
cidades["MG"] = 29229.88
cidades["ES"] = 27165.48
cidades["OUTROS"] = 19849.53


for tl_cidades in cidades:
    soma += cidades[tl_cidades]


for vl_cidade in cidades:
    result = cidades[vl_cidade] / soma
    print(f"A cidade de {vl_cidade} teve um percentual de {round(result*100,2)}%")



