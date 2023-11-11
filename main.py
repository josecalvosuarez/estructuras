import random

def generar_random(x, y):
    return random.randint(x, y)

print("Numero aleatorio: {}".format(generar_random(1, 100)))

d = dict()

d["cervecita"] = "Imperial"
d["campeon"] = "LDA"

print(d)
