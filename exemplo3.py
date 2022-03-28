import matplotlib.pyplot as plp

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 3, 7, 5, 4, 8, 10, 4]

titulo = "Gráfico de barras"

eixox = "Eixo X"
eixoy = "Eixo Y"

plp.title(titulo)
plp.xlabel(eixox)
plp.ylabel(eixoy)
plp.bar(x, y)
plp.show()
