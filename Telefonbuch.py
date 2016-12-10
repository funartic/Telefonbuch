'''
Created on 10.12.2016

@author: Daniel
'''
from view.MainFrame import MainFrame

class Telefonbuch():
    
    @staticmethod
    def main():
        root = MainFrame()
        root.set_window_default_size()
        root.mainloop()


if __name__ == '__main__':
    Telefonbuch.main()
    
    
    