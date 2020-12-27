import logging

# create logger
logger = logging.getLogger('module.submodule.core')


class TestModuleB:
    def __init__(self):
        self.logger = logging.getLogger('module.submodule.core.TestModuleB')
        self.logger.info('creating an instance of TestModuleB')

    def do_something(self):
        self.logger.info('doing something')
        p = 1 + 1
        self.logger.info('done doing something')
        return p


def some_function():
    logger.debug("this is module.submodule.core")
    logger.info("this is module.submodule.core")
    logger.warning("this is module.submodule.core")
    logger.error("this is module.submodule.core")
    logger.fatal("this is module.submodule.core")
