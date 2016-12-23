'''
Created on 10.12.2016

@author: Daniel
'''

from tkinter import Menu, filedialog

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
        helpmenu.add_command(label="About...", command=self.show_about())
        menubar.add_cascade(label="Help", menu=helpmenu)
        master.config(menu=menubar)
        
    def show_help(self):
        pass
    
    def show_about(self):
        pass