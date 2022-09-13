import csv

import time

import datetime

def trivia():
    
    # Lee los archivos

    csvfile = open('pregunta.csv', 'r')
    data = list(csv.DictReader(csvfile))
    csvfile.close()

    print('A continuación, indique los nombres de los jugadores:')
    # procedo a preguntar cuantos jugadores desean jugar
    jugador_1 = str(input('Jugador 1, ingrese su nombre:'))
    jugador_2 = str(input('Jugador 2, ingrese su nombre:'))


    # asignando variables
    puntaje_1 = 0
    puntaje_2 = 0
    
    numero_pregunta = 1
    numero_respuesta = 4

    juegodetrivia = 1

    # jugadorlist_1 = () # listado de respuestas jugador 1
    # jugadorlist_2 = () # Listado de respuestas jugador 2
    
    while True:
        for i in data:
            print('Pregunta numero {}:'.format(numero_pregunta))
            
            print(i['preguntas'])
            
            print('1)', i['1'])
            print('2)', i['2'])
            print('3)', i['3'])
            print('4)', i['4'])
            numero_pregunta +=1         


if __name__ == '__main__':
    print('Bienvenidos a nuestro juego de trivia')

jugar = (input('Desean jugar: \n1 SI.\n2 NO. \nIngrese la opcion correcta: '))

     # bucle para verificar que el valor ingresado sea el correcto
while jugar !='1' and jugar !='2':
    jugar = (input('Opcion erronea.\nIngrese 1 para jugar o 2 para terminar: '))
if jugar =='1':
    trivia()   
else: print('Adios.')

                

       
