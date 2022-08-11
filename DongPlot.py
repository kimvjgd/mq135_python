import serial
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



serialport = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=2)


class DongPlot():
  def __init__(self):
    self.x_vals = [0,0.1]
    self.y_vals = [0,600]
    self.index = count()


  
  def animate(self, i):
    self.x_vals.append(next(self.index)*0.2)
    # self.y_vals.append(random.randint(0,500))
    mq_value = serialport.readline()
    if str(mq_value) == "b\'\\r\\n\'":
      self.y_vals.append(0)
      pass
    else:
      print(int(str(mq_value)[2:5]))
      self.y_vals.append(int(str(mq_value)[2:5]))

      plt.cla()
      plt.plot(self.x_vals, self.y_vals, label="CO2")
      
      plt.legend(loc='upper left')
      plt.tight_layout()