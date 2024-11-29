import logging

logging.basicConfig(
    # file name for logging the data
    filename = 'app.log',
    filemode= 'w',   # writing on the file app.log
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S'
)
