import matplotlib.pyplot as plp

x = [1, 2, 3, 4]
y = [4, 6, 9, 10]
z = [ 600, 100, 450,1]

titulo = "Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"


plp.title(titulo)
plp.xlabel(eixox)
plp.ylabel(eixoy)
          
plp.plot(x,y, color = "b", linestyle = 'dotted')
plp.scatter(x,y, label  = "os pontos",color='chocolate',marker = "_",s=z)
plp.legend()
plp.show()