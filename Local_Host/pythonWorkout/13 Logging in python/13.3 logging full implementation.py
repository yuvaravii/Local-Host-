import logging


# setting basic config
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

log1  = logging.getLogger("MathsApp")

def add(a,b):
    result = a+b
    log1.debug(f"Addition of {a} + {b} = {result}")
    return result


def sub(a,b):
    result = a-b
    log1.debug(f"subtraction of {a} + {b} = {result}")
    return result

def div(a,b):
    try:
        result = a/b
        log1.debug(f"subtraction of {a} + {b} = {result}")
        return result
    except ZeroDivisionError:
        log1.error("Zero Division error, check denominator")
        return None


add(5,3)
sub(5,3)
div(5,6)