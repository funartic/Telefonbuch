from tkinter import Frame, Label, Entry
from tkinter.constants import E


class LeftSidePanel(Frame):
    
    lbl_fields = ['Vorname', 'Nachname', 'Strasse',
                  'Postleitzahl', 'Stadt', 'Telefon']
    
    def __init__(self, master, cnf={}, **kw):
        Frame.__init__(self, master, cnf, **kw)
        self.grid()
        self.configure(background='#141f1f')
        self.create_form()

    def create_form(self):
        for value in range(len(self.lbl_fields)):
            
            empty = Label(self)
            empty.configure(background='#141f1f', fg="White")
            empty.grid(columnspan=2)
            
            label1 = Label(self, text=self.lbl_fields[value])
            label1.configure(background='#141f1f', fg="White")
            # sticky = E (EAST) -> place to right
            label1.grid(row=value,  column=0, sticky=E)
            
            entry1 = Entry(self)
            entry1.grid(row=value,  column=1)
    
    
        

        
        
        