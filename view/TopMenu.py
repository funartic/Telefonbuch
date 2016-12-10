'''
Created on 10.12.2016

@author: Daniel
'''
from tkinter import Menu

class TopMenue(Menu):
    '''
    classdocs
    '''


    def __init__(self, master):
        '''
        Constructor
        '''
        Menu.__init__(self, master)
        subMenu = Menu(self)
        self.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Add Data", command=self.doNothing())
        
        
    def doNothing(self):
        print("OKAYYYY")