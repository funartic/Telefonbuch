from tkinter import Frame, Label, Entry, Button
from tkinter.constants import E, LEFT


class LeftSidePanel(Frame):
    
    lbl_fields = ['Vorname', 'Nachname', 'Strasse',
                  'Postleitzahl', 'Stadt', 'Telefon']
    
    def __init__(self, master, cnf={}, **kw):
        Frame.__init__(self, master,  borderwidth=1, **kw)
        self.configure(background='#141f1f')
        self.create_form()

    def create_form(self):
        for value in range(len(self.lbl_fields)):
            
            empty = Label(self)
            empty.configure(background='#141f1f', fg="White")
            empty.pack()
            
            label1 = Label(self, text=self.lbl_fields[value])
            label1.configure(background='#141f1f', fg="White")
            # sticky = E (EAST) -> place to right
            label1.pack()
            
            entry1 = Entry(self)
            entry1.pack()
    
            
        empty = Label(self)
        empty.configure(background='#141f1f', fg="White")
        empty.pack()
        
        btn_add = Button(self, text="Hinzufuegen")
        btn_add.pack()
        
        for i in range(10):
            empty = Label(self)
            empty.configure(background='#141f1f', fg="White")
            empty.pack()
        
        

        
        
        