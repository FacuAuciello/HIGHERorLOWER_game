#Juego higher or lower
import random

#Metricas de seguidores en instagram julio 2025. Cifras en millones
diccionario_juego = {
    "Selena Gomez": 429,
    "Nike": 306,
    "Cristiano Ronaldo": 639,
    "PlayStation": 32,
    "Dwayne Johnson": 396,
    "Ariana Grande": 379,
    "National Geographic": 283,
    "Lionel Messi": 504,
    "Kim Kardashian": 364,
    "Taylor Swift": 284,
    "Real Madrid CF": 127,
    "LeBron James": 159,
    "Xbox": 15,
    "Justin Bieber": 295,
    "FC Barcelona": 124,
    "Vin Diesel": 102,
    "Kylian Mbappé": 122,
    "NASA": 95,
    "Shakira": 91,
    "Will Smith": 76,
    "Snoop Dogg": 82,
    "Leonardo DiCaprio": 61,
    "Sergio Ramos": 59,
    "Louis Vuitton": 57,
    "Stephen Curry": 55,
    "MrBeast": 54,
    "Travis Scott": 53,
    "Gucci": 51,
    "Conor McGregor": 47,
    "Bad Bunny": 46,
    "Free Fire": 41,
    "FIFA": 38,
    "Lewis Hamilton": 37,
    "BMW": 36,
    "Apple": 34,
    "Netflix": 32,
    "Adidas": 29,
    "Versace": 29,
    "Ferrari": 27,
    "Adam Sandler": 23,
    "Rafael Nadal": 21,
    "Kevin Durant": 21,
    "Apex Legends": 19,
    "Valentino Rossi": 19,
    "League of Legends": 17,
    "GoPro": 17,
    "Serena Williams": 16,
    "Xbox": 15,
    "Fortnite": 14,
    "Max Verstappen": 13,
    "Ibai": 12,
    "Nintendo": 8,
    "Minecraft": 6,
    "Fernando Alonso": 5,
    "McDonald's": 4,
    "Coca-Cola": 3,
    "Counter-Strike": 3,
    "Pepsi": 2,
    "Maluma": 58
}

def dos_elementos_random():
    elementos_random = random.sample(list(diccionario_juego.keys()), 2) #dame una lista de 2 elementos random
    return elementos_random

def seleccion_de_opcion(elementos_random):
    opcionA, opcionB = elementos_random
    print(f"A: {opcionA}")
    print(f"B: {opcionB}")
    eligiendo_opcion = input("Quien tiene mas seguidores en instagram? A o B --> ")
    
    seguidores_opcion_A = diccionario_juego[opcionA]
    seguidores_opcion_B = diccionario_juego[opcionB]
    if eligiendo_opcion.upper() == "A" and seguidores_opcion_A > seguidores_opcion_B:
        print(f"BIEN PA! {opcionA} tiene {diccionario_juego[opcionA]}M, {opcionB} tiene {diccionario_juego[opcionB]}M")
    elif eligiendo_opcion.upper() == "B" and seguidores_opcion_B > seguidores_opcion_A:
        print(f"BIEN PA! {opcionB} tiene {diccionario_juego[opcionB]}M, {opcionA} tiene {diccionario_juego[opcionA]}M")
    elif eligiendo_opcion.upper() in ["A", "B"] and seguidores_opcion_A == seguidores_opcion_B: #Se puede crear la lista literal/coleccion inmediata cuando defino el if/elif/elfse #es lo mismo que hacer esto eligiendo_opcion.upper() == "A" or eligiendo_opcion.upper() == "B"
        print(f"BIEN SAFASTE! {opcionA}:{diccionario_juego[opcionA]}M y {opcionB}:{diccionario_juego[opcionB]}M tienen los mismos seguidores")
    else:
        print(f"Te equivocaste {opcionA} tiene {diccionario_juego[opcionA]}M seguidores y {opcionB} tiene {diccionario_juego[opcionB]}M seguidores")


seleccion_de_opcion(dos_elementos_random())


