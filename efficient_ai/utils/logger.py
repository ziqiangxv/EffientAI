# -*- coding: utf-8 -*-

''''''

import logging

console_handlers = []

def LOGGER(name: str = 'EfficientAI') -> logging.Logger:
    ''''''

    #logging.basicConfig(level = logging.DEBUG, stream = sys.stdout)
    logger = logging.getLogger(name = name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - \
            %(funcName)s - %(lineno)d - %(message)s')

        file_handler = logging.FileHandler("logger.txt")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        console_handlers.append(console_handler)

    return logger


def set_logger_level(level: str) -> bool:
    '''
    level should be 'DEBUG' or 'INFO' or 'WARNING' or 'ERROR' 
    '''

    ret = False

    if level == 'DEBUG':
        logger_level = logging.DEBUG
        ret = True
        
    elif level == 'INFO':
        logger_level = logging.INFO
        ret = True

    elif level == 'WARNING':
        logger_level = logging.WARNING
        ret = True

    elif level == 'ERROR':
        logger_level = logging.ERROR
        ret = True

    if ret:
        for console_handler in console_handlers:
            console_handler.setLevel(logger_level)
    else:
        logger = LOGGER()
        logger.error("ERROR: level should be 'DEBUG' or 'INFO' or 'WARNING' or 'ERROR'\n")

    return ret

