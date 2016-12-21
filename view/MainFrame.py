'''
Created on 10.12.2016

@author: Daniel
'''
from tkinter import Tk, Label
from view.LeftSidePanel import LeftSidePanel
from tkinter.constants import LEFT, SUNKEN, W, BOTTOM, X, Y, TOP, YES
from view.TopMenu import TopMenue
from view.TopSidePanel import TopSidePanel
from view.BottomSidePanel import BottomSidePanel



class MainFrame(Tk):
    
    def __init__(self):
        Tk.__init__(self)  # call super constructor
        self.title('Das Telefonbuch')
        self.configure(background='#141f1f')
        
#         ********* Toolbar *********
        self.top_menu = TopMenue(self)
        self.config(menu=self.top_menu)

#         ********* Status Bar *********
        self.status = Label(self, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        
#         ********* Left Side *********
        self.leftSidePanel = LeftSidePanel(self)
        self.leftSidePanel.pack(side=LEFT, fill=X)
        
#         ********* Top Side *********
        self.topSidePanel = TopSidePanel(self)
        self.topSidePanel.pack(side=TOP, fill=X, expand=YES, padx=80,)

#         ********* Right Side *********
        self.botSidePanel = BottomSidePanel(self)
        self.botSidePanel.pack(side=BOTTOM, anchor=W, fill=X, expand=YES)

    def setWindowSize(self, sLeft, sTop, sWidth, sHeight):
        self.wm_geometry(sWidth + "x" + sHeight + "+" + sLeft + "+" + sTop)

    def set_window_default_size(self):
        sLeft = "%s" % 20  # X-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sTop = "%s" % 20  # Y-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sWidth = "%s" % 800  # Breite (Pixels)
        sHeight = "%s" % 600  # Hoehe   (Pixels)
        self.setWindowSize(sLeft, sTop, sWidth, sHeight)
