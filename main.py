import matplotlib.pyplot as plt
from DongPlot import *

alarm = 'off'
dongplot = DongPlot()
ani = FuncAnimation(plt.gcf(), dongplot.animate, interval=50)
plt.show()
  