import os
import datetime
import psutil
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

Time = []
CPU = []
Memory = []
Disk = []
fig , (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
def main():
    ax1.set_ylim(0, 100)
    ax2.set_ylim(0, 100)
    ax3.set_ylim(0, 100)
    ax1.set_title('CPU Usage')
    ax2.set_title('Memory Usage')
    ax3.set_title('Disk Usage')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CPU %')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Memory %')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Disk %')
    ani = FuncAnimation(plt.gcf(), cmdplot, interval = 1000)
    plt.show()

def cmdplot(i):
    Time.append(datetime.datetime.now())
    CPU.append(psutil.cpu_percent())
    Memory.append(psutil.virtual_memory()[2])
    Disk.append(psutil.disk_usage('/')[3])
    ax1.plot(Time, CPU, color='blue')
    ax2.plot(Time, Memory, color='green')
    ax3.plot(Time, Disk, color='orange')

if __name__ == '__main__':
    main()