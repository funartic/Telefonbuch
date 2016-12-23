'''
Created on 19.12.2016

@author: Daniel
'''
import sys, os
import logging
from tkinter import Toplevel, Label


class Person(object):
        def __init__(self, firstname, secondname, streetname,
                     plz, city, phone_number):
            self.firstname = firstname
            self.secondname = secondname
            self.streetname = streetname
            self.plz = plz
            self.city = city
            self.phone_number = phone_number
            
        def to_string(self):
            return str(self.firstname)      + ";" \
                    + str(self.secondname)    + ";" \
                    + str(self.streetname)    + ";" \
                    + str(self.plz)           + ";" \
                    + str(self.city)          + ";" \
                    + str(self.phone_number)
        


class Model(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.path = ""
        
        
    def get_phone_list_as_array(self) -> []:
        dir_path = os.path.dirname(sys.modules['__main__'].__file__)
        array = []
        
        if(len(self.path) == 0):
            self.path = str(dir_path) + "\\resources\\Phonelist.txt"
            
        with open(self.path, "r", encoding="utf8") as ins:
            for line in ins:
                array.append(str(line).replace("\n", "").split(";"))
        return array
    
    
    def set_path_to_file_with_person_list(self, path):
        self.path = path
        
    
    def addPerson(self, person: Person):
        if(person.firstname.replace(" ", "") != "" and
           person.secondname.replace(" ", "") != "" and
           person.phone_number.replace(" ", "") != ""):
            logging.info(self.path)
            logging.info(person.to_string() + " =>" + " Adding...")
            with open(self.path, "a", encoding="utf8") as myfile:
                myfile.write(person.to_string())
                myfile.write('\n')
        else:
                toplevel = Toplevel()
                toplevel.title("Zur Info:")
                label1 = Label(toplevel, text="Bitte geben Sie den \
                Vornamen, Nachnamen und \
                die Telefonnummer an!", height=0, width=100)
                label1.pack()
            
            
    def deletePerson(self, person: Person):
        logging.info(person.to_string() + " =>" + " Deleting...")
        
        with open(self.path,'r', encoding="utf8") as file:
            lines = file.readlines()
            
        with open(self.path,'w', encoding="utf8") as file:
            for line in lines:
                if line !=person.to_string() + "\n":
                    file.write(line)
    
    def editPerson(self, old_person, new_person):
        logging.info(str(old_person.to_string()) + " => " 
                     + str(new_person.to_string))
        with open(self.path, 'r', encoding="utf8") as file:
            # read a list of lines into data
            data = file.readlines()
        
        for i in range(len(data)-1):
            if(data[i] == old_person.to_string()+"\n"):
                data[i] = new_person.to_string()+"\n"
                
        with open(self.path, 'w', encoding="utf8") as file:
            file.writelines( data )
                
    def set_path(self, path):
        self.path = path
            
    
            
            
