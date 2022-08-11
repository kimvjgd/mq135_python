import serial
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter.messagebox as msgbox
from tkinter import *
import time

root = Tk()
root.title("EDL LAB")
root.geometry('640x480')


# alarm
alarm_value = 400
alarm_range = 100

serialport = serial.Serial('/dev/cu.usbserial-10', 9600, timeout=2)

root.mainloop()

def create_new_file():
  print('파일을 새로 생성합니다.')

# File Menu
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command = create_new_file)
menu_file.add_command(label="New Window", command = create_new_file)
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


menu.add_cascade(label="Edit")

root.config(menu=menu)
root.mainloop()


class DongPlot():
  def __init__(self):
    self.x_vals = [0,0.1]
    self.y_vals = [0,600]
    self.index = count()
    # off, alarm_window, on
    self.alarm = "off"


  
  def animate(self, i):
    self.x_vals.append(next(self.index)*0.2)
    # self.y_vals.append(random.randint(0,500))
    mq_value = serialport.readline()
    if str(mq_value) == "b\'\\r\\n\'":
      self.y_vals.append(0)
      pass
    else:
      int_mq_value = int(str(mq_value)[2:5])
      print(int_mq_value)

      
      self.y_vals.append(int_mq_value)

      plt.cla()
      plt.plot(self.x_vals, self.y_vals, label="CO2")
      
      plt.legend(loc='upper left')
      plt.tight_layout()
      
      if int_mq_value < 300 and self.alarm == 'off':
        CO2info()
        self.alarm = "alarm_window"
        
def CO2info():
  msgbox.askokcancel("Y / N", "EDL LAB\n\n측정을 계속하시겠습니까?")



if __name__ == "__main__":
  dongplot = DongPlot()
  ani = FuncAnimation(plt.gcf(), dongplot.animate, interval=50)
  plt.show()


