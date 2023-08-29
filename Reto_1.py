from math import floor
cobro = float(0)
div = 0
d = int(input(f'Digite el dia en el que use el estacionamiento (del 1 al 7)'))
tiempo = int(input(f'Digite el tiempo del estacionamiento en minutos'))
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes", "Sabado", "Domingo"]
d = d-1
if(d == 0 or d == 1 or d == 2):
    if(tiempo >= 5 and tiempo <=60):
        cobro = 0
    else:
        div = tiempo/60
        cobro = 2*div
        cobro = floor(cobro)

elif(d == 3 or d == 4):
    if(tiempo >= 5 and tiempo <=60):
        cobro = 0
    else:
        div = tiempo/60
        cobro = 2.5*div
elif(d == 5 or d == 6):
    if(tiempo >= 5 and tiempo <=60):
        cobro = 0
    else:
        div = tiempo/60
        cobro = 3*div
        cobro = floor(cobro)

print(f'Dia: {dias[d]}      Tiempo: {tiempo} minutos')
print(f'su cobro es de: ${cobro}')