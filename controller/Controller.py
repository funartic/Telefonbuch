__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from view.MainFrame import MainFrame
from model.Model import Model, Person
from tkinter.constants import END
from tkinter import filedialog

class Controller(object):
    '''
    This class controlls the model and the view. 
    If any event is needed to handle this class will do it.
    It is the interface between model and view and update the 
    model after every change.
    '''
    
    table_entries = []

    def __init__(self):
        self.view = MainFrame(self)
        self.model = Model()
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        self.view.botSidePanel.bind("<Double-Button-1>", self.on_tree_edit)
        self.view.leftSidePanel.btn_add.bind("<Button-1>", self.add_person_btn_pressed)
        self.new_person = Person ("","","","","","")
        
    def showView(self):
        """ This method start the view"""
        self.view.set_window_default_size()
        self.view.resizable(0, 0)
        self.view.mainloop()
        
        
#      Event Handlings:
        
    def on_tree_edit(self, event):
        """ 
        If you double click on item in tree view, this method 
        shows a new window and enter the selected values in the entrys
        """
        curItem = self.view.botSidePanel.tree.focus()
        item_values = self.view.botSidePanel.tree.item(curItem)['values']
        old_person = Person(item_values[0], item_values[1], item_values[2],
                        item_values[3], item_values[4], item_values[5])
        self.view.botSidePanel.open_edit_view(old_person)

            
    def edit_person_btn_pressed(self, event):
        """ 
        This method take the input of the user to edit the person.
        It connects the view with the model.
        """
        curItem = self.view.botSidePanel.tree.focus()
        item_values = self.view.botSidePanel.tree.item(curItem)['values']
        old_person = Person(item_values[0], item_values[1], item_values[2],
                        item_values[3], item_values[4], item_values[5])
        self.new_person = Person (
            self.view.botSidePanel.edt_entry_first_name.get(),
            self.view.botSidePanel.edt_entry_second_name.get(),
            self.view.botSidePanel.edt_entry_street_name.get(),
            self.view.botSidePanel.edt_entry_plz.get(),
            self.view.botSidePanel.edt_entry_city.get(),
            self.view.botSidePanel.edt_entry_phone_number.get()
        )
        if(self.new_person.firstname != ""
           and self.new_person.secondname != ""
           and self.new_person.phone_number != ""):
            self.model.editPerson(old_person, self.new_person)
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        self.view.botSidePanel.edit_toplevel.destroy()
        
        
    def add_person_btn_pressed(self, event):
        """ 
        This method take the input of the user to add the person.
        It connects the view with the model.
        """
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
        """ 
        This method take the input of the user by the checkboxes.
        So you can specify the search. After finding the keyword it
        refresh the view of the tree.
        It connects the view with the model.
        """
        search_list = []
        keyword = self.view.topSidePanel.sv.get()
        if(keyword == ""):
            self.view.botSidePanel.set_table_content(self.table_entries)
        else:
            for array in self.table_entries:
                if((str(array[0]).startswith(keyword) and self.view.topSidePanel.checkBoxA.get()) or
                   (str(array[1]).startswith(keyword) and self.view.topSidePanel.checkBoxB.get()) or
                   (str(array[2]).startswith(keyword) and self.view.topSidePanel.checkBoxC.get()) or
                   (str(array[3]).startswith(keyword) and self.view.topSidePanel.checkBoxD.get()) or
                   (str(array[4]).startswith(keyword) and self.view.topSidePanel.checkBoxE.get()) or
                   (str(array[5]).startswith(keyword) and self.view.topSidePanel.checkBoxF.get())):
                    search_list.append(array)
                    self.view.botSidePanel.set_table_content(search_list)
                    
    def clear_entrys(self):
        """ This method only clear all entries from the left side panel"""
        self.view.leftSidePanel.entry_firstname.delete(0,END)
        self.view.leftSidePanel.entry_secondname.delete(0,END)
        self.view.leftSidePanel.entry_streetname.delete(0,END)
        self.view.leftSidePanel.entry_plz.delete(0,END)
        self.view.leftSidePanel.entry_city.delete(0,END)
        self.view.leftSidePanel.entry_phone_number.delete(0,END)
        
    def openFile(self):
        """ This method open a new file and set the content in the tree view"""
        self.model.set_path(filedialog.askopenfilename())
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        
    def on_tree_delete(self, event):
        """ 
        This method is activated by selecting an item of the tree
        and pressing the delte button. After doing that the item
        will be deleted from the file and the view refreshs.
        It connects the view with the model.
        """
        curItem = self.view.botSidePanel.tree.focus()
        item_values = self.view.botSidePanel.tree.item(curItem)['values']
        person = Person(item_values[0], item_values[1], item_values[2],
                        item_values[3], item_values[4], item_values[5])
        self.model.deletePerson(person)
        self.table_entries = self.model.get_phone_list_as_array()
        self.view.botSidePanel.set_table_content(self.table_entries)
        