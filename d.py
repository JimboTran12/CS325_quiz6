from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

class LoggingLibraryLogger(Logger):
    def debug(self, message):
        # Implement debug logging
        print("Debug:", message)

    def info(self, message):
        # Implement info logging
        print("Info:", message)

    def warning(self, message):
        # Implement warning logging
        print("Warning:", message)

    def error(self, message):
        # Implement error logging
        print("Error:", message)

class Application:
    def __init__(self, logger):
        self.logger = logger

    def do_something(self):
        # Example application logic
        self.logger.debug("Doing something...")

if __name__ == "__main__":
    # Using loguru as the logging library
    logger = LoggingLibraryLogger()
    app = Application(logger)
    app.do_something()
