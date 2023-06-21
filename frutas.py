# Programa que me diga de qué fruta se trata por medio de sus caracteristicas
frutas = {
    "manzana": {
        "color": "rojo",
        "tamaño": "mediano",
        "forma": "redonda"
    },
    "naranja": {
        "color": "naranja",
        "tamaño": "mediano",
        "forma": "redonda"
    },
    "plátano": {
        "color": "amarillo",
        "tamaño": "grande",
        "forma": "alargada"
    },
    "pera": {
        "color": "verde",
        "tamaño": "mediano",
        "forma":  "ovalada"
    },
    "sandía": {
        "color": "verde",
        "tamaño": "grande",
        "forma": "redonda"
    }
}

# Solicitamos características de las frutas
color = input("¿De qué color es la fruta? ")
tamaño = input("¿De qué tamaño es la fruta? ")
forma = input("¿Qué forma tiene la fruta? ")

# Comparamos las características de la fruta con las otras disponibles
for fruta, caracteristicas in frutas.items():
    if color == caracteristicas["color"] and tamaño == caracteristicas["tamaño"] and forma == caracteristicas["forma"]:
        print("La fruta es una", fruta)
        break
else:
    print("No se reconoce la fruta.")
