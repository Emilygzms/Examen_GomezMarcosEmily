#Número Capicúa

num=int(input("Datos de Entrada:"))
num_str=str(num)
cantidad_digi=len(num_str)

if(cantidad_digi%2==0):
    vueltas=int(cantidad_digi/2)
    acumulador=0
    for i in range(vueltas):
        if(num_str[i]==num_str[cantidad_digi-i-1]):
            acumulador+=1

        if(acumulador==vueltas):
            print("Si es capicúa")

        else:
            print("No es capicúa")   