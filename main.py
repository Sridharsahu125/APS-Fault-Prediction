from senser.exception import SenserException
from senser.logger import logging
import os
import sys

def test_exception():
    try:
        logging.info("yaha pe error ayega")
        a=1/0
    except Exception as e:
        raise SenserException(e,sys)
    
if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)        
            