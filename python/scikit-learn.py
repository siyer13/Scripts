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

>>> from sklearn.linear_model import LinearRegression
>>> X = [[6], [8], [10], [14], [18]]
>>> Y = [[7], [9], [13], [17.5], [20]]
>>> model = LinearRegression()
>>> model.fit(X,Y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
>>> print ('A 12inch pizza should cost: $%.2f' % model.predict([12][0]))
A 12inch pizza should cost: $14.20
