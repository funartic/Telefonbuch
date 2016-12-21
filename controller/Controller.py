'''
Created on 19.12.2016

@author: Daniel
'''
from view.MainFrame import MainFrame
from model.Model import Model
import logging

class Controller(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.view = MainFrame()
        self.model = Model()
        self.view.botSidePanel.set_table_content(self.model.get_phone_list_as_array())
        
        
    def showView(self):
        self.view.set_window_default_size()
        self.view.resizable(0, 0)
        self.view.mainloop()