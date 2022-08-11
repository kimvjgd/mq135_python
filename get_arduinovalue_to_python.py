import serial
from DongPlot import *
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


serialport = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=2)

# off, alarm_window, on
alarm = "off"


dongplot = DongPlot()
index = count()


while True:
  
  mq_value = serialport.readline()
  # print(mq_value)
  # except for initial trash value 
  if str(mq_value) == "b\'\\r\\n\'":
    pass
  else:
    print(int(str(mq_value)[2:5]))
    dongplot.x_vals.append(next(index))
    dongplot.y_vals.append(int(str(mq_value)[2:5]))
    if int(str(mq_value)[2:5]) < 400:
      alarm = "alarm_window"
      print('under 400 : '+str(mq_value)[2:5])

    # print(str(mq_value)[2:5])
    else:
      print('over 400 : '+str(mq_value)[2:5])
    if alarm == True:
      print('On!!!')
    # try:
    #   print(int(str(mq_value)[2:5]))
    # except:
    #   print('error')
    
    ani = FuncAnimation(plt.gcf(), dongplot.animate, interval=100)

    
  print(dongplot.x_vals)
  print(dongplot.y_vals)
  plt.show()



