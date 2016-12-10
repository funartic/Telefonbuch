'''
Created on 10.12.2016

@author: Daniel
'''
from tkinter import Tk, Label
from view.LeftSidePanel import LeftSidePanel
from tkinter.constants import LEFT, SUNKEN, ANCHOR, W, BOTTOM, X
from view.BuckysButton import MyClass
from view.TopMenu import TopMenue



class MainFrame(Tk):
    
    def __init__(self):
        Tk.__init__(self)  # call super constructor
        self.title('Das Telefonbuch')
        self.configure(background='#141f1f')
        
        # ********* Toolbar *********
        top_menu = TopMenue(self)
        self.config(menu=top_menu)
        
        # ********* Left Side *********
        b = MyClass(self)
        
        # ********* Right Side *********
        
        # ********* Status Bar *********
        status = Label(self, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

    def setWindowSize(self, sLeft, sTop, sWidth, sHeight):
        self.wm_geometry(sWidth + "x" + sHeight + "+" + sLeft + "+" + sTop)

    def set_window_default_size(self):
        sLeft = "%s" % 20  # X-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sTop = "%s" % 20  # Y-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sWidth = "%s" % 800  # Breite (Pixels)
        sHeight = "%s" % 600  # Hoehe   (Pixels)
        self.setWindowSize(sLeft, sTop, sWidth, sHeight)
