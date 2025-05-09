"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
 ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""


vl_verefiicar = int(input("Digite o valor desejeado para checagem: " ))

x = 0
sequencia_fibonacci_one = 0
sequencia_fibonacci_twe = 1
sequencia_fibonacci_three = 0
sequencia_list = [1]

while vl_verefiicar > sequencia_fibonacci_one:
    sequencia_fibonacci_three = sequencia_fibonacci_one
    sequencia_fibonacci_one += sequencia_fibonacci_twe
    sequencia_fibonacci_twe = sequencia_fibonacci_three

    print(sequencia_fibonacci_one)
    sequencia_list.append(sequencia_fibonacci_one)


if vl_verefiicar in sequencia_fibonacci_one:
    print(f"Valor inserido {vl_verefiicar} está na lista de Fibonacci")



