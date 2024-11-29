from logger import logging 

def addition(a,b):

    logging.debug("Here the addition process is taking place")
    return a+b


logging.debug("The addition function is called outside")
addition(15,16)