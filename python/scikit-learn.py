>>> import matplotlib.pyplot as plt
>>> X = [[6], [8], [10], [14], [18]]
>>> Y = [[7], [9], [13], [17.5], [20]]
>>> plt.figure()
<Figure size 640x480 with 0 Axes>
>>> plt.title('Pizza price plotted against diameter')
Text(0.5,1,'Pizza price plotted against diameter')
>>> plt.xlabel('Diameter in inches')
Text(0.5,0,'Diameter in inches')
>>> plt.ylabel('Price in dollars')
Text(0,0.5,'Price in dollars')
>>> plt.plot(X,Y,'k.')
[<matplotlib.lines.Line2D object at 0x7f8dea3666d8>]
>>> plt.axis([0,25,0,25])
[0, 25, 0, 25]
>>> plt.grid(True)
>>> plt.show()

