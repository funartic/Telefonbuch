'''
Created on 10.12.2016

@author: Daniel
'''
from tkinter import Frame, Button
from tkinter.constants import LEFT

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, master):
        '''
        Constructor
        '''
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="asdasd", command=master.quit)
        self.printButton.pack(side=LEFT, padx= 3, pady=3)
        
        