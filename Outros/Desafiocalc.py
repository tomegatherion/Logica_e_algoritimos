
def calc_medidas_do_triangulo(x1, x2, x3, y1, y2, y3):
  a = calc_distancia_euclidiana(x1,y1,x2,y2)
  b = calc_distancia_euclidiana(x2,y2,x3,y3)
  c = calc_distancia_euclidiana(x1,y1,x3,y2)
  perimetro = calc_perimetro_do_triangulo(a, b, c)
  area = calc_area_do_triangulo(a, b, c, perimetro)
  return perimetro, area



def calc_distancia_euclidiana(x1,y1,x2,y2):
  return(((x2 - x1) ** 2) + ((y3 - y1) ** 2)) ** .5


def calc_perimetro_do_triangulo(a,b,c):
  return a+b+c


def calc_area_do_triangulo(a,b,c, perimetro):
  p=perimetro / 2
  return((p*p-a)*(p-b)*(p-c))**.5


x1=1
x2=4
x3=2
y1=1
y2=4
y3=2

(perimetro, area) = calc_medidas_do_triangulo(x1,x2,x3,y1,y2,y3)
print(f'Perímetro do triângulo:{perimetro}')
print(f'Área do triângulo:{area}')