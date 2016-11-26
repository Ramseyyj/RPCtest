import xmlrpc.client
from tkinter import *
import tkinter.messagebox


def time_to_string(time_m):

    time_m = '%s' % time_m

    year = time_m[0:4]
    month = time_m[4:6]
    day = time_m[6:8]
    hour = time_m[9:11]
    minute = time_m[12:14]
    second = time_m[15:17]

    return '%s-%s-%s %s:%s:%s' % (year, month, day, hour, minute, second)


class MainWindow:

    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def tick(self):
        # get the current local time from the PC
        time_g = s.getServerTime()
        time_string = time_to_string(time_g)
        # if time string has changed, update it
        self.clock.config(text=time_string)
        self.clock.after(500, self.tick)

    def __init__(self):
        self.frame = Tk()
        self.frame.title('show server time')
        self.center_window(self.frame, 300, 60)

        self.clock = Label(self.frame, font=('times', 20, 'bold'), bg='green')
        self.clock.pack()
        self.tick()

        self.frame.mainloop()


s = xmlrpc.client.ServerProxy('http://192.168.159.129:8000')

window = MainWindow()

# Print list of available methods
# print(s.system.listMethods())
