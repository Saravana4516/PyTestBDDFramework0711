import logging


def LoggingMessage (self) :
    logger = logging.getLogger(__name__)
    fileHandler = logging. FileHandler('logfile, Log')
    formatter = logging. Formatter ("%(asctime)s :%(Levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler (fileHandler)
    logger.setLevel(logging.INFO)
    return logger