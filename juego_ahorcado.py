###############################-- M O D U L O S

import random

###############################-- F U N C I O N E S
# ------------- Esta función nos representa el dibujo del ahorcado, y el VALOR de la funcion nos irá sacando el dibujo segun la cantidad de fallos
def dibujo(valor):
    print(ahorcado[valor])

# ------------- Creamos la función de palabra aleatoria
def buscar_palabra_aleatoria(lista_palabras):
    palabra = random.randint(0, len(lista_palabras))
    return lista_palabras[palabra]

# ------------- Funcion de ganar la partida
def victoria():
    print("""
             __    __       ___           _______.     _______      ___      .__   __.      ___       _______    ______    __   __   __  
            |  |  |  |     /   \         /       |    /  _____|    /   \     |  \ |  |     /   \     |       \  /  __  \  |  | |  | |  | 
            |  |__|  |    /  ^  \       |   (----`   |  |  __     /  ^  \    |   \|  |    /  ^  \    |  .--.  ||  |  |  | |  | |  | |  | 
            |   __   |   /  /_\  \       \   \       |  | |_ |   /  /_\  \   |  . `  |   /  /_\  \   |  |  |  ||  |  |  | |  | |  | |  | 
            |  |  |  |  /  _____  \  .----)   |      |  |__| |  /  _____  \  |  |\   |  /  _____  \  |  '--'  ||  `--'  | |__| |__| |__| 
            |__|  |__| /__/     \__\ |_______/        \______| /__/     \__\ |__| \__| /__/     \__\ |_______/  \______/  (__) (__) (__)
            """)

# ------------- Funcion de perder la partida
def derrota():
    print("""
             __    __       ___           _______.   .______    _______ .______       _______   __   _______    ______    __   __   __    
            |  |  |  |     /   \         /       |   |   _  \  |   ____||   _  \     |       \ |  | |       \  /  __  \  |  | |  | |  |   
            |  |__|  |    /  ^  \       |   (----`   |  |_)  | |  |__   |  |_)  |    |  .--.  ||  | |  .--.  ||  |  |  | |  | |  | |  | 
            |   __   |   /  /_\  \       \   \       |   ___/  |   __|  |      /     |  |  |  ||  | |  |  |  ||  |  |  | |  | |  | |  | 
            |  |  |  |  /  _____  \  .----)   |      |  |      |  |____ |  |\  \----.|  '--'  ||  | |  '--'  ||  `--'  | |__| |__| |__|  
            |__|  |__| /__/     \__\ |_______/       | _|      |_______|| _| `._____||_______/ |__| |_______/  \______/  (__) (__) (__) 
            """)

def empezar():
    print("""
        **************************
         ¡¡ EMPIEZA LA PARTIDA !!
        **************************
        """)

###############################-- L I S T A S

lista_palabras = [
    "gato",
    "perro",
    "raton",
    "elefante",
    "tigre",
    "leon",
    "bombilla",
    "led",
    "mariposa",
    "hombre",
    "mujer",
    "hervivoro",
    "patata",
    "zanahoria",
    "almohada",
    "sillon",
    "sifon",
    "mascarilla",
    "supermercado",
    "compra",
    "idea",
    "idealista",
    "superacion",
    "adorno",
    "navidad",
    "arbol",
    "campanilla",
    "bosque",
    "selva",
    "llanura",
    "playa",
    "montaña",
    "gigante",
    "anciano",
    "dios",
    "sexualidad",
    "amarillo",
    "divulgacion",
    "señorial",
    "demonio",
    "colegio",
    "sarten",
    "huesped",
    "locura",
]
lista_espacios = []
ahorcado = [
    """
                        +---+
                        |   |
                            |
                            |
                            |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                            |
                            |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                       /|   |
                            |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                       /|\  |
                            |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                       /|\  |
                       /    |
                            |
                        =========""",
    """
                        +---+
                        |   |
                        O   |
                       /|\  |
                       / \  |
                            |
                        =========""",
]
lista_introducidas = []

###############################-- V A R I A B L E S

repetir = True
intentos = 6
repeticion = True
nombre = input("Introduce tu nombre: ")

###############################-- P R O G R A M A

# ------------- Iniciamos el bucle que nos pedirá nuevas partidas has que no queramos jugar más.

print("¡Hola!,",nombre)

while repeticion:
    repetir = input("¿Quieres jugar una nueva partida?(S/N)")
    repetir = repetir.lower()

    if repetir == "s":
        # ------------- Creamos las variables que se limpiarán en cada partida nueva
        palabra_aleatoria = buscar_palabra_aleatoria(lista_palabras)
        palabra_aleatoria = list(palabra_aleatoria)
        espacios = len(palabra_aleatoria)
        contador_dibujo = 0
        lista_espacios.clear()
        lista_introducidas.clear()

    # ------------- Creamos la lista de espacios que se irá cambiando al acertar el jugador
        for i in range(len(palabra_aleatoria)):
            lista_espacios.append("_" * 1)

        # ------------- Nos muestra un texto como que empieza la partida
        empezar()

        # ------------- Empezamos el bucle para rellenar la palabra
        while repetir:

            # ------------- Pedimos al usuario la letra
            letra_usuario = input("Introduce una letra: ")
            letra_usuario = letra_usuario.lower()
            # ------------- Si la letra no está en la lista de introducidas, la añadimos
            if letra_usuario not in lista_introducidas:
                lista_introducidas.append(letra_usuario)
            # ------------- Si la letra está en la lista de introducidas, lo indicamos y volvemos a pedir una letra.
            else:
                print("La letra ya ha sido introducida!")
                print("Estas son las letras que has introducido: ",lista_introducidas)
                letra_usuario = input("Introduce una letra: ")

            # ------------- Recorremos la palabra aleatoria
            for h in range(len(palabra_aleatoria) - 1, -1, -1):
                letra_añadir = palabra_aleatoria[h]
                # ------------- Si la letra coincide, sustituimos el "_" por la letra
                if letra_añadir.startswith(letra_usuario):
                    lista_espacios.pop(h)
                    lista_espacios.insert(h, palabra_aleatoria[h])
                # ------------- Le decimos que cuando no queden "_" en la lista salga del bucle
                elif "_" not in lista_espacios:
                    repetir = False
                    victoria()

            # ------------- Cuando la letra del usuario no este en la palabra aleatoria, imprime la varible del dibujo y suma 1 al contador del dibujo
            if letra_usuario not in palabra_aleatoria:
                print(dibujo(contador_dibujo))
                print(nombre,"TE QUEDAN:",(intentos - contador_dibujo),"intentos.")
                contador_dibujo += 1

            # ------------- Cuando el contador es mayor que el nº de intentos ya se habrá mostrado el ultimo dibujo. Informamos de la muerte y el bucle termina.
            if contador_dibujo > intentos:
                repetir = False
                derrota()
            print(lista_espacios)
        # ------------- Informamos al jugador de cual era su palabra a adivinar
        print(nombre,"La palabra era:",palabra_aleatoria)
        repeticion = True
        
    elif repetir == "n":
        print("¡OK!,",nombre,"jugaremos en otro momento.")
        repeticion = False
    else:
        print(nombre,"Introduce una respuesta válida")
        repeticion = True


