import logging
from logging.handlers import TimedRotatingFileHandler
import module.submodule.core
import module.utils

LOG_FILE = "example.log"


def getLogger(file_name):
    FORMAT = r'%(asctime)s %(levelname)-8s %(name)s[line:%(lineno)d] - %(message)s'
    # create logger with 'module'
    logger = logging.getLogger('module')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = TimedRotatingFileHandler(filename=LOG_FILE, when="D", interval=1)
    # fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(FORMAT)
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)

    return logger


logger = getLogger(LOG_FILE)

if __name__ == "__main__":
    logger.debug("this is main")
    logger.info("this is main")
    logger.warning("this is main")
    logger.error("this is main")
    logger.fatal("this is main")

    logger.info('creating an instance of module.utils.TestModuleA')
    o1 = module.utils.TestModuleA()
    logger.info('created an instance of module.utils.TestModuleA')
    logger.info('calling module.utils.TestModuleA.do_something')
    o1.do_something()
    logger.info('finished module.utils.TestModuleA.do_something')
    logger.info('calling module.utils.some_function()')
    module.utils.some_function()
    logger.info('done with module.utils.some_function()')

    logger.info('creating an instance of module.submodule.core.TestModuleB')
    o2 = module.submodule.core.TestModuleB()
    logger.info('created an instance of module.submodule.core.TestModuleB')
    logger.info('calling module.submodule.core.TestModuleB.do_something')
    o2.do_something()
    logger.info('finished module.submodule.core.TestModuleB.do_something')
    logger.info('calling module.submodule.core.some_function()')
    module.submodule.core.some_function()
    logger.info('done with module.submodule.core.some_function()')
