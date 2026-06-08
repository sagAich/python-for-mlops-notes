# This file is to demonstrate the use of logger.exception() method.
# A common MLOps/backend pattern is:
#try:
#    # risky operation
#except Exception:
#    logger.exception("Something failed")
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

class rotatingFileHandlerDemo:
    def sample_rotating_file_handler(self):

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        rotating_handler = RotatingFileHandler(
        "size_based.log",
        maxBytes=1024,
        backupCount=5)

        timed_handler = TimedRotatingFileHandler(
        "time_based.log",
        when="midnight",
        interval=1,
        backupCount=5)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
            datefmt="%Y-%m-%d %H:%M:%S")
        
        rotating_handler.setFormatter(formatter)
        timed_handler.setFormatter(formatter)

        logger.addHandler(rotating_handler)
        logger.addHandler(timed_handler)
        
        try:
            logger.info("application started")

            # intention error
            result = 10 / 0
            logger.info(f"result: {result}")

        except Exception:
            logger.exception("An error occurred")
        finally:
            for handler in list(logger.handlers):
                handler.close()
                logger.removeHandler(handler)

if __name__ == "__main__":
    rfhd = rotatingFileHandlerDemo()
    rfhd.sample_rotating_file_handler()