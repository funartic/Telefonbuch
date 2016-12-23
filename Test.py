__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from model.Model import Model, Person
import os, sys


def main():
    """
    Awesome tests!!!
    """
    model = Model()
    
    person = Person("firstname", "secondname", "streetname",
                     "plz", "city", "phone_number")
    new_person = Person("firstnam1e", "secondname1", "streetname1",
                     "plz1", "city1", "phone_number1")
    
    model.set_path(os.path.dirname(sys.modules['__main__'].__file__)+ "\\resources\\Phonelist.txt")
    
#   file got a new person  
    model.addPerson(person)
#   new person is deleted..
    model.deletePerson(person)
#   file got a new person again..
    model.addPerson(person)
#   this time we edit the person
    model.editPerson(person, new_person)
    
#   this looks like it works. :)
#   We have no clue how to test gui

if __name__ == '__main__':
    main()