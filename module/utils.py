import logging

# create logger
logger = logging.getLogger('module.utils')


class TestModuleA:
    def __init__(self):
        self.logger = logging.getLogger('module.utils.TestModuleA')
        self.logger.info('creating an instance of TestModuleA')

    def do_something(self):
        self.logger.info('doing something')
        p = 1 + 1
        self.logger.info('done doing something')
        return p


def some_function():
    logger.debug("this is module.utils")
    logger.info("this is module.utils")
    logger.warning("this is module.utils")
    logger.error("this is module.utils")
    logger.fatal("this is module.utils")
