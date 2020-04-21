INFO=3
WARN=2
ERROR=1

def print_log(level:int, msg: str, *args, **kwargs ):
    print(msg.format(*args, **kwargs))

logger = print_log

def log(msg: str, *args, **kwargs ):
    logger(INFO, msg, *args, **kwargs)

def warn(msg: str, *args, **kwargs ):
    logger(WARN, msg, *args, **kwargs)

def error(msg: str, *args, **kwargs ):
    logger(ERROR, msg, *args, **kwargs)