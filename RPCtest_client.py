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

    def buttonListener1(self, event):

        def tick():
            # get the current local time from the PC
            time_g = s.getServerTime()
            time_string = time_to_string(time_g)
            # if time string has changed, update it
            clock.config(text=time_string)
            clock.after(200, tick)

        root = Tk()
        clock = Label(root, font=('times', 20, 'bold'), bg='green')
        clock.grid(row=0, column=1)
        tick()
        root.mainloop()

    def buttonListener2(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 2 dialog")

    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def __init__(self):
        self.frame = Tk()
        self.frame.title('show server time')
        self.center_window(self.frame, 300, 120)

        self.button1 = Button(self.frame, text="digital mode", width=12, height=2)
        self.button2 = Button(self.frame, text="analogue mode", width=20, height=2)

        self.button1.pack(padx=20, side='left')
        self.button2.pack(padx=10, side='right')

        self.button1.bind("<ButtonRelease-1>", self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>", self.buttonListener2)

        self.frame.mainloop()


s = xmlrpc.client.ServerProxy('http://192.168.159.129:8000')

window = MainWindow()

# Print list of available methods
# print(s.system.listMethods())
