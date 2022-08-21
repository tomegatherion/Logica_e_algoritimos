# Desafio 8

op_validos = ('+', '-', '*', '/')

while True:
    e = input('Digite o valor a esquerda do operador: ')
    op = input(f'Digite o operador. Opções: {op_validos}')
    d = input('Digite p valor a direita do operador: ')
    if op in op_validos and e.isnumeric() and d.isnumeric():
        if op == '/' and d == '0':
          print('Divisão por zero! Tente novamente.')
          continue
        expressão = e + ' ' + op + ' ' + d
        print(e, op, d, "=", eval(expressão))
        break
    print("Valores ou operado incorreto!")