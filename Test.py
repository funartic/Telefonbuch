'''
Created on 22.12.2016

@author: Daniel
'''
from model.Model import Model, Person
import os, sys


def main():
    model = Model()
    
    person = Person("firstname", "secondname", "streetname",
                     "plz", "city", "phone_number")
    new_person = Person("firstnam1e", "secondname1", "streetname1",
                     "plz1", "city1", "phone_number1")
    
    model.set_path(os.path.dirname(sys.modules['__main__'].__file__)+ "\\resources\\Phonelist.txt")
    
    model.addPerson(person)
    model.deletePerson(person)
    model.editPerson(person, new_person)



if __name__ == '__main__':
    main()