# This file is to show that how to use rotatingfilehandlers in the logging module in python.
# this module is used to create log files that rotate when they reach a certain size or at a certain time interval.
# there are two types of rotating file handlers available in the logging module, which are:
# 1. RotatingFileHandler: This handler rotates the log file based on its size.
# 2. TimedRotatingFileHandler: This handler rotates the log file based on time intervals.
import logging
class rotatingFileHandlerDemo:
    def sample_rotating_file_handler(self):
        from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
        # creating a logger object
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG) # setting the logging level to DEBUG
        # creating a rotating file handler object
        rotating_handler = RotatingFileHandler("size_based.log", maxBytes=1024*1024, backupCount=5) 
        # maxBytes=1024*1024 means 1 MB, backupCount=5 means keep 5 backup files
        # creating a timed rotating file handler object
        timed_handler = TimedRotatingFileHandler("time_based.log", when="midnight", interval=1, backupCount=5)
        # when="midnight" means the handler will roll over and start writing logs to a new log file at exactly 12:00 AM (00:00),
        # interval=1 means rotate every day, backupCount=5 means keep 5 backup files.
        # creating a formatter object
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        # adding the formatter to the handlers
        rotating_handler.setFormatter(formatter)
        timed_handler.setFormatter(formatter)
        # adding the handlers to the logger
        logger.addHandler(rotating_handler)
        logger.addHandler(timed_handler)
        # now we can use the logger object to create log messages using debug(), info(), warning(), error() and critical() methods.
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")
        # output:
        # 2024-06-30 12:00:00 - __main__ - DEBUG - debug log statement
        # 2024-06-30 12:00:00 - __main__ - INFO - info log statement
        # 2024-06-30 12:00:00 - __main__ - WARNING - warning log statement
        # 2024-06-30 12:00:00 - __main__ - ERROR - error log statement
        # 2024-06-30 12:00:00 - __main__ - CRITICAL - critical log statement

        # When midnight hits, TimedRotatingFileHandler takes the existing time_based.log,
        # renames it by appending yesterday's date (e.g., time_based.log.2026-06-08), and creates a brand new,
        # empty time_based.log for the new day. It preserves your history and will keep up to
        # 5 days of history because of backupCount=5. On the 6th night, the oldest file is deleted.

        # Day 1:  time_based.log                  ← active file

        # Day 2:  time_based.log                  ← new active file. here the logs for day 2026-06-10 will be stored.
        # time_based.log.2026-06-09               ← Day 1 renamed

        # Day 3:  time_based.log                  ← new active file
        # time_based.log.2026-06-10               ← Day 2 renamed
        # time_based.log.2026-06-09               ← Day 1

        # Day 4:  time_based.log                  ← new active file
        # time_based.log.2026-06-11               ← Day 3 renamed
        # time_based.log.2026-06-10               ← Day 2
        # time_based.log.2026-06-09               ← Day 1
 
        # Day 5:  time_based.log                  ← new active file
        # time_based.log.2026-06-12               ← Day 4 renamed
        # time_based.log.2026-06-11               ← Day 3
        # time_based.log.2026-06-10               ← Day 2
        # time_based.log.2026-06-09               ← Day 1
 
        # Day 6:  time_based.log                  ← new active file
        # time_based.log.2026-06-13               ← Day 5 renamed
        # time_based.log.2026-06-12               ← Day 4
        # time_based.log.2026-06-11               ← Day 3
        # time_based.log.2026-06-10               ← Day 2
        # time_based.log.2026-06-09               ← Day 1  ← DELETED on Day 7

        # Day 7:  time_based.log                  ← new active file
        # time_based.log.2026-06-15               ← Day 6
        # time_based.log.2026-06-14               ← Day 5
        # time_based.log.2026-06-13               ← Day 4
        # time_based.log.2026-06-12               ← Day 3
        # time_based.log.2026-06-11               ← Day 2  ← DELETED on Day 8


        # If the size of the log file exceeds 1 MB, the log file will be rotated and
        # a new log file will be created with the names size_based.log.1, size_based.log.2, etc.

        # For a small script this is okay. For production code you usually close handlers:
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        # especially when applications shut down.
        # before cleanup:
        # Logger(__main__)
        # │
        # ├── RotatingFileHandler
        # └── TimedRotatingFileHandler
        # After cleanup: logger has no handlers
        # Logger(__main__)
        # │
        # └── No handlers
        # Now imagine a scenario for the following code:
        # logger.addHandler(rotating_handler)
        # logger.addHandler(timed_handler)
        # raise Exception("Something broke!")
        # for handler in list(logger.handlers):
        # handler.close()
        # logger.removeHandler(handler)
        # The exception occurs before cleanup.
        # So the handlers stay attached.
        # Logger now looks like:
        # Logger(__main__)
        # │
        # ├── RotatingFileHandler
        # └── TimedRotatingFileHandler
        # Next Call Now you run:
        # rfhd.sample_rotating_file_handler()
        # Now logger contains:
        # Logger(__main__)
        # │
        # ├── RotatingFileHandler   (old)
        # ├── TimedRotatingFileHandler (old)
        # ├── RotatingFileHandler   (new)
        # └── TimedRotatingFileHandler (new)
        # A production-grade version would use:
        # try:
        #     logger.debug("debug log statement")
        #     logger.info("info log statement")
        #     logger.warning("warning log statement")
        #     logger.error("error log statement")
        #     logger.critical("critical log statement")
        # finally:
        #     for handler in list(logger.handlers):
        #         handler.close()
        #         logger.removeHandler(handler)


if __name__ == "__main__":
    rfhd = rotatingFileHandlerDemo()
    rfhd.sample_rotating_file_handler()
