__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from tkinter import Tk, Label
from view.LeftSidePanel import LeftSidePanel
from tkinter.constants import LEFT, SUNKEN, W, BOTTOM, X, TOP, YES
from view.TopMenu import TopMenue
from view.TopSidePanel import TopSidePanel
from view.BottomSidePanel import BottomSidePanel



class MainFrame(Tk):
    """ 
    This class is the root window and 
    collects every single panel.
    Sadly we couldn't find another way to give the MainFrame(view) the
    controller.  >:(
    For advice how to do the mvc pattern in python we would be happy.
    But it is not necessary needed :)
    There are also some configuration made.
    """
    
    def __init__(self, controller):
        Tk.__init__(self)  # call super constructor
        self.title('Das Telefonbuch')
        self.configure(background='#141f1f')
        
#         ********* Toolbar *********
        self.top_menu = TopMenue(self, controller)

#         ********* Status Bar *********
        self.status = Label(self, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        
#         ********* Left Side *********
        self.leftSidePanel = LeftSidePanel(self)
        self.leftSidePanel.pack(side=LEFT, fill=X)
        
#         ********* Top Side *********
        self.topSidePanel = TopSidePanel(self, controller)
        self.topSidePanel.pack(side=TOP, fill=X, expand=YES, padx=80,)

#         ********* Right Side *********
        self.botSidePanel = BottomSidePanel(self, controller)
        self.botSidePanel.pack(side=BOTTOM, anchor=W, fill=X, expand=YES)

    def setWindowSize(self, sLeft, sTop, sWidth, sHeight):
        """
         This method sets the size of the root window.
        """
        self.wm_geometry(sWidth + "x" + sHeight + "+" + sLeft + "+" + sTop)

    def set_window_default_size(self):
        """
         This method sets the default size of the root window.
        """
        sLeft = "%s" % 20  # X-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sTop = "%s" % 20  # Y-Position auf dem Bildschirm (linke obere Ecke in Pixels)
        sWidth = "%s" % 800  # Breite (Pixels)
        sHeight = "%s" % 600  # Hoehe   (Pixels)
        self.setWindowSize(sLeft, sTop, sWidth, sHeight)
