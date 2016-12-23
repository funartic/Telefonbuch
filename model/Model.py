__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

import sys, os
import logging
from tkinter import Toplevel, Label


class Person(object):
    """ Only a container class """
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
    This class is the real backend. 
    Its methods are activated by the controller (see MVC-pattern).
    It mainly do some change on the file.
    '''

    def __init__(self):
        self.path = ""
        
        
    def get_phone_list_as_array(self) -> []:
        """ Reads the file and return a list"""
        dir_path = os.path.dirname(sys.modules['__main__'].__file__)
        array = []
        
        if(len(self.path) == 0):
            self.path = str(dir_path) + "\\resources\\Phonelist.txt"
            
        with open(self.path, "r", encoding="utf8") as ins:
            for line in ins:
                array.append(str(line).replace("\n", "").split(";"))
        return array
    
    
    def set_path_to_file_with_person_list(self, path):
        """ 
        Set the path to the file
        which is read
        """
        self.path = path
        
    
    def addPerson(self, person: Person):
        """ Adds a new Person to the file"""
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
        """ 
        Delete an existing Person of the file
        by searching for this person and write the file new
        except the person the user deleted.
        """
        logging.info(person.to_string() + " =>" + " Deleting...")
        
        with open(self.path,'r', encoding="utf8") as file:
            lines = file.readlines()
            
        with open(self.path,'w', encoding="utf8") as file:
            for line in lines:
                if line !=person.to_string() + "\n":
                    file.write(line)
    
    def editPerson(self, old_person, new_person):
        """ 
        Edit an existing Person of the file by searching the old one
        and write the file again.
        """
        logging.info(str(old_person.to_string()) + " => " 
                     + str(new_person.to_string()))
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
            
    
            
            
