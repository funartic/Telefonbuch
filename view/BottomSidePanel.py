from tkinter import Frame
import tkinter.ttk as ttk
import tkinter.font as tkFont


class BottomSidePanel(Frame):
    
    def __init__(self, master,controller, cnf={}, **kw):
        Frame.__init__(self, master,  borderwidth=1, **kw)
        self.configure(background='#141f1f')
        self.controller = controller
        self.create_form()

    def create_form(self):
        self.tree = ttk.Treeview(columns=tbl_header, show="headings")
        self.tree.bind("<Double-Button-1>", self.controller.on_tree_select)
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
        self.tree.delete(*self.tree.get_children())
        for item in table_content_list:
            index = table_content_list.index(item, )
            self.tree.insert('', 'end', values=item, text=index)
#           adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(tbl_header[ix],width=None)<col_w:
                    self.tree.column(tbl_header[ix], width=col_w)
        
                    
                    
#     def on_tree_select(self, event):
#             print("selected item:", end="", flush=True)
#             for item in self.tree.selection():
#                 item_text = self.tree.item(item, "text")
#                 print(item_text)
#                     
# 
def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))
    

tbl_header = ['Vorname', 'Nachname', 'Strasse',
              'Postleitzahl', 'Stadt', 'Telefon']