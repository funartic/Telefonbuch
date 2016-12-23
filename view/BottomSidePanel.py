__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"


from tkinter import Frame, Toplevel, Label, Entry, Button
import tkinter.ttk as ttk
import tkinter.font as tkFont


class BottomSidePanel(Frame):
    """
    This panel got the main element: The tree view
    """
    def __init__(self, master,controller, cnf={}, **kw):
        Frame.__init__(self, master,  borderwidth=1, **kw)
        self.configure(background='#141f1f')
        self.controller = controller
        self.create_form()

    def create_form(self):
        self.tree = ttk.Treeview(columns=tbl_header, show="headings")
        self.tree.bind("<Double-Button-1>", self.controller.on_tree_edit)
        self.tree.bind("<Delete>", self.controller.on_tree_delete)
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self)
        vsb.grid(column=1, row=0, sticky='ns', in_=self)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        hsb.grid(column=0, row=1, sticky='ew', in_=self)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set, height=25)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        for col in tbl_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))



    def set_table_content(self, table_content_list):
        """
        This method set the table content and
        adjust column's width if necessary to fit each value.
        But first we needed to delete the children, to be sure
        that we dont append children by refreshing the table.
        BTW: It is possible to add alphabetical number to 
        phone number in case for plus or minus symbols:
        +0176 or 1231-4123-1412
        """
        self.tree.delete(*self.tree.get_children())
        for item in table_content_list:
            index = table_content_list.index(item, )
            self.tree.insert('', 'end', values=item, text=index)
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(tbl_header[ix],width=None)<col_w:
                    self.tree.column(tbl_header[ix], width=col_w)
        
    def open_edit_view(self, old_person):
        """
        This method opens a new popup window and
        set for all entries the specific values.
        """
        self.edit_toplevel = Toplevel()
        self.edit_toplevel.title("Editieren:")
        
        self.edt_lbl_first_name = Label(self.edit_toplevel, text=tbl_header[0])
        self.edt_lbl_first_name.grid(row=0, column=0)
        self.edt_entry_first_name = Entry(self.edit_toplevel)
        self.edt_entry_first_name.insert(0,old_person.firstname)
        self.edt_entry_first_name.grid(row=0, column=3)
        
        self.edt_lbl_second_name = Label(self.edit_toplevel, text=tbl_header[1])
        self.edt_lbl_second_name.grid(row=1, column=0)
        self.edt_entry_second_name = Entry(self.edit_toplevel)
        self.edt_entry_second_name.insert(0,old_person.secondname)
        self.edt_entry_second_name.grid(row=1, column=3)
        
        self.edt_lbl_street_name = Label(self.edit_toplevel, text=tbl_header[2])
        self.edt_lbl_street_name.grid(row=2, column=0)
        self.edt_entry_street_name = Entry(self.edit_toplevel)
        self.edt_entry_street_name.insert(0,old_person.firstname)
        self.edt_entry_street_name.grid(row=2, column=3)
        
        self.edt_lbl_plz = Label(self.edit_toplevel, text=tbl_header[3])
        self.edt_lbl_plz.grid(row=3, column=0)
        self.edt_entry_plz = Entry(self.edit_toplevel)
        self.edt_entry_plz.insert(0,old_person.plz)
        self.edt_entry_plz.grid(row=3, column=3)
        
        self.edt_lbl_city = Label(self.edit_toplevel, text=tbl_header[4])
        self.edt_lbl_city.grid(row=4, column=0)
        self.edt_entry_city = Entry(self.edit_toplevel)
        self.edt_entry_city.insert(0,old_person.city)
        self.edt_entry_city.grid(row=4, column=3)
        
        self.edt_lbl_phone_number = Label(self.edit_toplevel, text=tbl_header[5])
        self.edt_lbl_phone_number.grid(row=5, column=0)
        self.edt_entry_phone_number = Entry(self.edit_toplevel)
        self.edt_entry_phone_number.insert(0,old_person.firstname)
        self.edt_entry_phone_number.grid(row=5, column=3)
        
        self.btn_edit_person = Button(self.edit_toplevel, text="Editieren")
        self.btn_edit_person.grid(row=6, column=2)
        self.btn_edit_person.bind("<Button-1>", 
                                  self.controller.edit_person_btn_pressed)
        
                    
def sortby(tree, col, descending):
    """ 
    This FUNCTION sorts the tree contents as soon 
    as a column header is clicked on
    """
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
#     switch the heading so it will sort in the opposite direction
#     credits to: http://stackoverflow.com/questions/1796469/
#     how-to-sort-tree-view-on-click-on-column-header
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))
    
# for lazy ppl we tried to create the view elements dynamically
# using a for loop. But we found no way to access events on them then.
tbl_header = ['Vorname', 'Nachname', 'Strasse',
              'Postleitzahl', 'Stadt', 'Telefon']