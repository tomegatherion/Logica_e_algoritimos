import time


umidade_interna = ()
temperatura_interna = ()
temperatura_externa = ()
botão_pronto = (0)


print("Iniciando Forno.")
umidade_interna = float(input("Digite a umidade interna do forno: "))
temperatura_interna = float(input("Digite a temperatura interna do forno: "))
temperatura_externa = float(input("Digite a temperatura externa do forno: "))

time.sleep(2)

def sensores():
  global umidade_interna
  umidade_interna = float(input("Digite a umidade interna do forno: "))
  global temperatura_interna
  temperatura_interna = float(input("Digite a temperatura interna do forno: "))
  global temperatura_externa
  temperatura_externa = float(input("Digite a temperatura externa do forno: "))


if temperatura_externa < 20 and umidade_interna > 40:
  print("Iniciando Desumidificação")
  if temperatura_interna > 15 and umidade_interna >= 40:
    print("Exaustor Ligado")
  if temperatura_interna < 15 and umidade_interna >= 40:
    temperatura_interna = 100
    print("Exaustor Ligado.\nAquecimento definido em 100ºC")
  if umidade_interna < 5:
    print("Exaustor Desligado")
else:
  print("Iniciando Cocção")
  if umidade_interna > 15:
      exaustor = True
  if temperatura_interna < 200:
      temperatura_interna = 380
  if umidade_interna < 5 and temperatura_interna >= 380:
      while botão_pronto == 0:
        print("Inserir contudo para cocção - quando concluir pressionar o botão pronto")
        botão_pronto = input("Pressione qualquer tecla para pressionar o pronto: ")
      print("Configurando tempo!")
      time.sleep(2)
      print("Forno em funcionamento")
      time.sleep(2)
      print("Tempo definido para 3 horas de cocção.")
      time.sleep(2)
      print("Tempo Restante 3:00")
      time.sleep(2)
      print("Tempo Restante 2:30")
      time.sleep(2)
      print("Tempo Restante 2:00")
      time.sleep(2)
      print("Tempo Restante 1:30")
      time.sleep(2)
      print("Tempo Restante 1:00")
      time.sleep(2)
      print("Tempo Restante 0:30")      
      time.sleep(2)
      print("Tempo Restante 0:01")
      time.sleep(2)
      print("Cocção concluida")
      print("Aquecimento desligado")

time.sleep(10)
sensores()
  

