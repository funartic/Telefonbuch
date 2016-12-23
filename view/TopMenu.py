__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from tkinter import Menu, Label, Toplevel
from tkinter.constants import LEFT, W

class TopMenue():
    '''
    classdocs
    '''


    def __init__(self, master, controller):
        '''
        Constructor
        '''
        self.controller = controller
        
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command= lambda: controller.openFile())
        menubar.add_cascade(label="File", menu=filemenu)
    
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command= lambda: self.show_help())
        helpmenu.add_command(label="About...", command= lambda: self.show_about())
        menubar.add_cascade(label="Help", menu=helpmenu)
        master.config(menu=menubar)
        
    def show_help(self):
        toplevel = Toplevel()
        toplevel.title("Die Hilfe:")
        label1 = Label(toplevel, text="Benutzbarkeit des Telefonbuchs:", height=0, width=100, anchor=W,  justify=LEFT)
        label1.pack()
        empty = Label(toplevel, text="", height=0, width=100)
        empty.pack()
        label2 = Label(toplevel, text="Zum Hinzufuegen:", height=0, width=100, anchor=W, justify=LEFT)
        label2.pack()
        label3 = Label(toplevel, text=
"Bitte fuellen Sie alle rosa Felder \
aus (Vornamen, Nachnamen, Telefon). Das sind die Pflichtfelder! Die \
die restlichen Felder sind", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label3.pack()
        label4 = Label(toplevel, text="optional.", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label4.pack()
        empty = Label(toplevel, text="", height=0, width=100)
        empty.pack()
        label5 = Label(toplevel, text="Zum Loeschen:", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label5.pack()
        label6 = Label(toplevel, text=
"Selektieren Sie das zu loeschende Feld\
 und druecken Sie die Entfernen-Taste!", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label6.pack()
        
        empty = Label(toplevel, text="", height=0, width=100)
        empty.pack()
        label7 = Label(toplevel, text="Zum Editieren:", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label7.pack()
        label8 = Label(toplevel, text=
"Fuehren Sie einen Doppelklick mit der linken Maustaste \
auf die zu editierende Zeile aus.", 
                       height=0, width=100, anchor=W, justify=LEFT)
        label8.pack()
        
    def show_about(self):
        toplevel = Toplevel()
        toplevel.title("About:")
        label1 = Label(toplevel, text=
"Made by: Kristiyan Ivanov, Daniel Holzinger"
                       , height=0, width=100, anchor=W,  justify=LEFT)
        label1.pack()
