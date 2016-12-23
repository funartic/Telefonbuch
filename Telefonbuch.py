'''
Created on 10.12.2016

@author: Daniel
'''
from controller.Controller import Controller
import logging
import sys

class Telefonbuch():
    
    @staticmethod
    def main():
        
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        logging.info('Started')
        controller = Controller()
        controller.showView()
        logging.info('Finished')

if __name__ == '__main__':
    Telefonbuch.main()
    