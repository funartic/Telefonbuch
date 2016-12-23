from tkinter import Frame, Label, Entry, Button, Checkbutton, StringVar
from tkinter.constants import LEFT, W


class TopSidePanel(Frame):
    
    lbl_fields = ['Vorname', 'Nachname', 'Strasse',
              'Postleitzahl', 'Stadt', 'Telefon']
        
    def __init__(self, master, controller, cnf={}, **kw):
        Frame.__init__(self, master,  borderwidth=1, **kw)
        self.configure(background='#141f1f')
        self.controller = controller
        self.create_form()

    def create_form(self):
        empty = Label(self)
        empty.configure(background='#141f1f', fg="White")
        empty.grid()
        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv= self.sv: self.controller.search_for_keyword(self.sv))
        input_search = Entry(self, width=59, textvariable=self.sv)
        input_search.grid(row=1, column=1, columnspan=9)
        empty = Label(self)
        empty.configure(background='#141f1f', fg="White")
        empty.grid()
        lbl_search = Button(self, text="Suche", fg="White")
        lbl_search.configure(background='#141f1f')
        lbl_search.grid(row=1, column=10)
        
        for i in range(len(self.lbl_fields)):
            checkbox = Checkbutton(self, 
                                   text=self.lbl_fields[i], 
                                   variable=i)
            checkbox.select()
            checkbox.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                            ,activeforeground='White', selectcolor='Black')
            checkbox.grid(row=2, column=i+2)
        

        
        
        