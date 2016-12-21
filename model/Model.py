'''
Created on 19.12.2016

@author: Daniel
'''
import sys, os
import fileinput
import logging


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
            return str(self.person.firstname)      + ";" \
                    + str(self.person.secondname)    + ";" \
                    + str(self.person.streetname)    + ";" \
                    + str(self.person.plz)           + ";" \
                    + str(self.person.city)          + ";" \
                    + str(self.person.phone_number)
        


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
        logging.info(person.to_string() + " =>" + " Adding...")
        with open(self.path, "a") as myfile:
            myfile.write(person.to_string() + '\n')
            
            
    def deletePerson(self, person: Person):
        logging.info(person.to_string() + " =>" + " Deleting...")
        for line in fileinput.input(self.path, inplace=True):
            if person.to_string() in line:
                continue
            print(line, end='')
            
    def editPerson(self, old_person, new_person):
        logging.info(old_person.to_string() + " => " + new_person.to_string)
        with open(self.path, 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        
        for i in range(len(data)-1):
            if(data[i] == old_person.to_string()):
                data[i] = new_person.to_string()
                
        with open(self.path, 'w') as file:
            file.writelines( data )
                
            
            
        
            
            
            
            
