#nome, telefone, idade, saldo,

def adicionar(lista):
    
    while True:
        nome = input("Digite o nome do Contato   ")
        if not existe_contato(lista, nome):
            break
        else:
            print("Esse contato já foi cadastrado.")
            print("Por favor, tente um novamente.")
    contato = {
        "nome": nome,
        "tel":  input("Digite o Telefone:   "),
        "idade": input(("Digite a Idade: ")),
        "saldo": input(("Digite o Saldo "))
    }
    lista.append(contato)
    print("O contato {} foi cadrastrado com sucesso!\n".format(contato['nome']))



def existe_contato(lista, nome):               
    if len(lista) > 0:
        for contato in lista:
            if contato['nome'] == nome:
                return True   
    return False



def listar(lista):
  print(" === Lista de Contatos === ")
  if len(lista) > 0:
      for i, contato in enumerate(lista):
        print("Contato {}:" .format(i+1))
        print("\tNome: {}" .format(contato['nome']))
        print("\tTelefone: {}" .format(contato['tel']))
        print("\tIdade: {}" .format(contato['idade']))
        print("\tSaldo: {}" .format(contato['saldo']))      
      print("Quantidade de contatos: {}\n" .format(len(lista)))
  else:
      print("Não existe nenhum contato cadastrado no sistema.\n")



def carregar_contatos():
    lista = []

    try:
        arquivo = open("contatos.txt", "r")
        for linha in arquivo.readlines():
            coluna = linha.strip().split(",")

            contato = {
                "nome": coluna[0],
                "tel": coluna[1],
                "idade":  coluna[2],
                "saldo": coluna[3]
        }

        lista.append(contato)
    except FileNotFoundError:
            pass
    return lista



def salvar_contatos(lista):
    if len(lista) > 0:

        arquivo = open("contatos.txt" , "w")
        for contato in lista:
            arquivo.write("{},{},{},{}\n" .format(contato['nome'], contato['tel'], contato['idade'], contato['saldo']))      
        arquivo.close()
        print("Relatório salvo com sucesso!")
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")




def principal():

    lista = carregar_contatos()  
    
    while True:
        print(" =========== Banco de Dados ============ ")
        print(" === Registro Cadastral Dos Clientes ===")
        print(" ======================================= ")
        print(" ===  1 - adicionar contato          ===")
        print(" ===  2 - listar contatos            ===")
        print(" ===  3 - Salvar contatos            ===")
        print(" ===  0 - sair                       ===")
        print(" ===                                 === ")
        print(" ===    Informe a Opção desejada     ===")
        print(" ======================================= ")

        opção = int(input("> "))

        if opção == 1:
            adicionar(lista)

        elif opção == 2:
          listar(lista)

        elif opção == 3:
          salvar_contatos(lista)

        elif opção == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção Inválida! Por favor, Selecione a Opção corretamente!!!\n")        
principal()