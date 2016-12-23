'''
Created on 19.12.2016

@author: Daniel
'''
from view.MainFrame import MainFrame
from model.Model import Model, Person
from tkinter.constants import END

class Controller(object):
    '''
    classdocs
    '''
    
    table_entries = []

    def __init__(self):
        self.view = MainFrame(self)
        self.model = Model()
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        self.view.botSidePanel.bind("<Double-Button-1>", self.on_tree_select)
        self.view.leftSidePanel.btn_add.bind("<Button-1>", self.add_person_btn_pressed)
        
    def showView(self):
        self.view.set_window_default_size()
        self.view.resizable(0, 0)
        self.view.mainloop()
        
        
#      Event Handlings:
        
    def on_tree_select(self, event):
        print("selected item:", end="", flush=True)
        for item in self.view.botSidePanel.tree.selection():
            item_text = self.view.botSidePanel.tree.item(item, "text")
            print(item_text)
            
    def add_person_btn_pressed(self, event):
        person = Person(''.join(e for e in self.view.leftSidePanel
                                .entry_firstname.get() if e.isalnum()),
                        ''.join(e for e in self.view.leftSidePanel
                                .entry_secondname.get() if e.isalnum()),
                        ''.join(e for e in self.view.leftSidePanel
                                .entry_streetname.get() if e.isalnum()),
                        ''.join(e for e in self.view.leftSidePanel
                                .entry_plz.get() if e.isalnum()),
                        ''.join(e for e in self.view.leftSidePanel
                                .entry_city.get() if e.isalnum()),
                        ''.join(e for e in self.view.leftSidePanel
                                .entry_phone_number.get() if e.isalnum())
                        )
        self.model.addPerson(person)
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        self.clear_entrys()
    
    def search_for_keyword(self, sv):
        search_list = []
        keyword = self.view.topSidePanel.sv.get()
        if(keyword == ""):
            self.view.botSidePanel.set_table_content(self.table_entries)
        else:
            for array in self.table_entries:
                if(str(array[0]).startswith(keyword)):
                    search_list.append(array)
                    self.view.botSidePanel.set_table_content(search_list)
                    
    def clear_entrys(self):
        self.view.leftSidePanel.entry_firstname.delete(0,END)
        self.view.leftSidePanel.entry_secondname.delete(0,END)
        self.view.leftSidePanel.entry_streetname.delete(0,END)
        self.view.leftSidePanel.entry_plz.delete(0,END)
        self.view.leftSidePanel.entry_city.delete(0,END)
        self.view.leftSidePanel.entry_phone_number.delete(0,END)
        
    def openFile(self):
        print("lol")
        

            
    def on_tree_delete(self, event):
        curItem = self.view.botSidePanel.tree.focus()
        item_values = self.view.botSidePanel.tree.item(curItem)['values']
        person = Person(item_values[0], item_values[1], item_values[2],
                        item_values[3], item_values[4], item_values[5])
        self.model.deletePerson(person)
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        