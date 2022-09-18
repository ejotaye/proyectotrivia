import csv

import time

import datetime

def trivia():
    
    # Lee los archivos

    csvfile = open('pregunta.csv')
    data = list(csv.DictReader(csvfile))
    csvfile.close()
    #print(data)

    print('A continuación, indique los nombres de los jugadores:')
    # procedo a preguntar cuantos jugadores desean jugar
    jugador_1 = str(input('Jugador 1, ingrese su nombre:'))
    jugador_2 = str(input('Jugador 2, ingrese su nombre:'))


    # asignando variables para puntajes
    puntaje_1 = 0
    puntaje_2 = 0
    
    # iniciamos en la pregunta numero 1
    numero_pregunta = 1
        
    # Empezamos a iterar las preguntas alojadas en nuestro archivo csv
    while True:
        for i in data:
            print('Pregunta numero {}:'.format(numero_pregunta))
            
            print(i['preguntas'])
            
            print('1)', i['1'])
            print('2)', i['2'])
            print('3)', i['3'])
            print('4)', i['4'])
            
            numero_pregunta +=1

            # Procedemos a realizar los input para la selección de cada jugador
            while True:
                resp_j1 = int(input('{}: Seleccione el número de la respuesta correcta:'.format(jugador_1)))

                if resp_j1 <= 0 or resp_j1 > 4:
                    print('Por favor selecciona una opción correcta')
                    resp_j1 = input('{}: Seleccione el número de la respuesta correcta:'.format(jugador_1))
                else:
                    pass

                resp_j2 = int(input('{}: Seleccione el número de la respuesta correcta:'.format(jugador_2)))

                if resp_j2 <= 0 or resp_j2 > 4:
                    print('Por favor selecciona una opción correcta')
                    resp_j2 = input('{}: Seleccione el número de la respuesta correcta:'.format(jugador_2))
                else:
                    break
            
            # Nombramos una variable para hacer print en pantalla de la respuesta correcta
            respuesta = i['respuesta_correcta']
            print('La respuesta correcta es: {}'.format(respuesta))

            # Realizamos condicionales para sumar puntos a los jugadores
            respuesta = int(respuesta)
            while True:
                if resp_j1 == respuesta:
                    puntaje_1 +=50
                    break
                if resp_j2 == respuesta:
                    puntaje_2 +=50
                else:
                    break

            # A continuación procedemos a concluir el ciclo de preguntar cerrando el bucle               
            if numero_pregunta == 4:
                break

        # Procedemos a reflejar el ganador anidando condicionales.        
        if puntaje_1 > puntaje_2:
            print('¡Felicidades! {} a ganado'.format(jugador_1))
            print('Lo siento {} ¡La proxima vez tendrás mas suerte!'.format(jugador_2))
        elif puntaje_2 > puntaje_1:
            print('¡Felicidades! El {} a ganado'.format(jugador_2))
            print('Lo siento {} ¡La proxima vez tendrás mas suerte!'.format(jugador_1))
        else:
            print('¡WOW! fue un empate, inténtalo nuevamente :D Mucha suerte.')

        # Creamos un archivo csv para alojar los puntajes históricos
        header =['jugador 1', 'puntaje1', 'jugador 2', 'puntaje2']
        csvfile = open('historico.csv', 'w')
        write = csv.DictWriter(csvfile, fieldnames=header)

        puntajes = {'jugador 1': jugador_1, 'puntaje1': puntaje_1, 'jugador 2': jugador_2, 'puntaje2': puntaje_2}

        write.writerow(puntajes)

        csvfile.close()
        break
            
            

    


        


if __name__ == '__main__':
    print('Bienvenidos a nuestro juego de trivia')

jugar = (input('Desean jugar: \n1 SI.\n2 NO. \nIngrese la opcion correcta: '))

     # bucle para verificar que el valor ingresado sea el correcto
while jugar !='1' and jugar !='2':
    jugar = (input('Opcion erronea.\nIngrese 1 para jugar o 2 para terminar: '))
if jugar =='1':
    trivia()   
else: print('Adios.')