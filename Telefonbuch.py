__author__ = "6252742: Daniel Holzinger, 6167921: Kristiyan Ivanov"
__copyright__ = "Copyright 2016/2017 – EPR-Goethe-Uni"

from controller.Controller import Controller
import logging
import sys

class Telefonbuch():
    """
    This class contains the main method.
    So the start point is here!
    """
    
    @staticmethod
    def main():
        """
        The main method.
        It configures the logger and after that 
        it initialize a controller which starts the gui. 
        """
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
    