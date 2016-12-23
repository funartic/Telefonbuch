__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from tkinter import Frame, Label, Entry, Button


class LeftSidePanel(Frame):
    """
    Boring class only implements some stupid view elements
    You can see the result on the left side of the root 
    window.
    """
    
    lbl_fields = ['Vorname', 'Nachname', 'Strasse',
                  'Postleitzahl', 'Stadt', 'Telefon']
    
    def __init__(self, master, cnf={}, **kw):
        Frame.__init__(self, master,  borderwidth=1, **kw)
        self.configure(background='#141f1f')
        self.create_form()

    def create_form(self):
        """
        See class describtion...
        """
#       firstname  
        self.lbl_firstname = Label(self, text=self.lbl_fields[0])
        self.lbl_firstname.configure(background='#141f1f', fg="White")
        self.lbl_firstname.pack()
        
        self.entry_firstname = Entry(self, bg="#D0AA90")
        self.entry_firstname.pack()
        
#       secondname  
        self.lbl_secondname = Label(self, text=self.lbl_fields[1])
        self.lbl_secondname.configure(background='#141f1f', fg="White")
        self.lbl_secondname.pack()
        
        self.entry_secondname = Entry(self, bg="#D0AA90")
        self.entry_secondname.pack()
        
#       streetname  
        self.lbl_streetname = Label(self, text=self.lbl_fields[2])
        self.lbl_streetname.configure(background='#141f1f', fg="White")
        self.lbl_streetname.pack()
        
        self.entry_streetname = Entry(self)
        self.entry_streetname.pack()
        
#       plz  
        self.lbl_plz = Label(self, text=self.lbl_fields[3])
        self.lbl_plz.configure(background='#141f1f', fg="White")
        self.lbl_plz.pack()
        
        self.entry_plz = Entry(self)
        self.entry_plz.pack()
        
#       city  
        self.lbl_city = Label(self, text=self.lbl_fields[4])
        self.lbl_city.configure(background='#141f1f', fg="White")
        self.lbl_city.pack()
        
        self.entry_city = Entry(self)
        self.entry_city.pack()
        
#       phone_number  
        self.lbl_phone_number = Label(self, text=self.lbl_fields[5])
        self.lbl_phone_number.configure(background='#141f1f', fg="White")
        self.lbl_phone_number.pack()
        
        self.entry_phone_number = Entry(self, bg="#D0AA90")
        self.entry_phone_number.pack()
        
            
        empty = Label(self)
        empty.configure(background='#141f1f', fg="White")
        empty.pack()
        
        self.btn_add = Button(self, text="Hinzufuegen")
        self.btn_add.pack()
        
#       Push the elements to the top.   
        for i in range(10):
            empty = Label(self)
            empty.configure(background='#141f1f', fg="White")
            empty.pack()
        
        

        
        
        