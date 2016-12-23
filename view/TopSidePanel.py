__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from tkinter import Frame, Label, Entry, Button, Checkbutton, StringVar,\
    BooleanVar


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
        
#         for i in range(len(self.lbl_fields)):
        self.checkBoxA = BooleanVar()
        self.checkbox_firstname = Checkbutton(self, 
                               text=self.lbl_fields[0], 
                               variable=self.checkBoxA)
        self.checkbox_firstname.select()
        self.checkbox_firstname.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_firstname.grid(row=2, column=0)
        
        self.checkBoxB = BooleanVar()
        self.checkbox_secondname = Checkbutton(self, 
                               text=self.lbl_fields[1], 
                               variable=self.checkBoxB)
        self.checkbox_secondname.select()
        self.checkbox_secondname.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_secondname.grid(row=2, column=3)
        
        self.checkBoxC = BooleanVar()
        self.checkbox_street = Checkbutton(self, 
                               text=self.lbl_fields[2], 
                               variable=self.checkBoxC)
        self.checkbox_street.select()
        self.checkbox_street.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_street.grid(row=2, column=5)
        
        self.checkBoxD = BooleanVar()
        self.checkbox_plz = Checkbutton(self, 
                               text=self.lbl_fields[3], 
                               variable= self.checkBoxD)
        self.checkbox_plz.select()
        self.checkbox_plz.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_plz.grid(row=2, column=7)
        
        self.checkBoxE = BooleanVar()
        self.checkbox_city = Checkbutton(self, 
                               text=self.lbl_fields[4], 
                               variable=self.checkBoxE)
        self.checkbox_city.select()
        self.checkbox_city.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_city.grid(row=2, column=9)
        
        self.checkBoxF = BooleanVar()
        self.checkbox_phone_number = Checkbutton(self, 
                               text=self.lbl_fields[5], 
                               variable=self.checkBoxF)
        self.checkbox_phone_number.select()
        self.checkbox_phone_number.config(bg='#141f1f', fg='White', activebackground='#141f1f'
                        ,activeforeground='White', selectcolor='Black')
        self.checkbox_phone_number.grid(row=2, column=10)
        

        

        
        
        