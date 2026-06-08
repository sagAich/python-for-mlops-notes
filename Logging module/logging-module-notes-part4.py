# this python file is to show how loggers, handlers and formatters work in the logging module in python.
# loggers are used to create log messages, handlers are used to send the log messages to different destinations,
#  and formatters are used to format the log messages.
# loggers, handlers and formatters are the three main components of the logging module in python.
# there are other approaches like:
# 1. creating a logging config file and reading it using logging.config.fileConfig() method.
# 2. creating a logging config dictionary and reading it using logging.config.dictConfig() method.

import logging
class loggerDemo:
    def sample_logger(self):
        # First step is to create a logger object, we can create a logger object using logging.getLogger() method.
        logger = logging.getLogger(__name__) 
        # __name__ is a variable that holds the name of the current module. When class loggerDemo is imported in another module, 
        # then __name__ will hold the name of the class that is "loggerDemo" and when it is executed as a standalone script or run directly, 
        # then __name__ will hold the value "__main__".

        # suppose inside my project i have
        # project/
        #  │
        #  ├── app1.py 
        #  ├── loggerDemo.py 
        #  └── database.py
        # if i remove the last two lines of the code in loggerDemo.py file, which are:
        # ld = loggerDemo() 
        # ld.sample_logger() 
        # And we write these lines inside app1.py and database.py, 
        # then when i execute app1.py and database.py, then the value of __name__ will be "loggerDemo",
        # and if i execute loggerDemo.py directly, then the value of __name__ will be "__main__".
        # But in this case no logs will be created for LoggerDemo.py file as i have removed the last two lines of the code.
        # ld = loggerDemo() 
        # ld.sample_logger()
        # which are responsible to create an object of the loggerDemo class and call the sample_logger() method.
        # Thus also to run the loggerDemo.py file as standalone script.
        # we have to write "if __name__ == "__main__":" prior to the last two lines of the code, 
        # and then we can execute the loggerDemo.py file directly as well.

        # next step is to set the logging level for the logger object, we can set the logging level using logger.setLevel() method.
        logger.setLevel(logging.DEBUG) # we can set the logging level to DEBUG, INFO, WARNING, ERROR, CRITICAL.
        # next step is to create a handler object.
        # there are different types of handlers available in the logging module, such as StreamHandler, FileHandler, etc.
        stream_handler = logging.StreamHandler() # this handler will send the log messages to the console.
        file_handler = logging.FileHandler("app.log", mode='w') # this handler will send the log messages to a file named app.log.
        # next step we have to create a formatter object, we can create a formatter object using logging.Formatter() method.
        # this will format the log messages in a specific way.
        # here we are using two formatter objects, one for the console handler and one for the file handler,
        #  we can use the same formatter object for both handlers as well.
        formatter = logging.Formatter(f"%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        formatter1 = logging.Formatter(f"%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # next step is to add the formatter object to console handler or file handler using setFormatter() method.
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter1)
        # next step is to add the handler object to the logger object using addHandler() method.
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        # now we can use the logger object to create log messages using debug(), info(), warning(), error() and critical() methods.
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")
ld = loggerDemo()
ld.sample_logger()

#output:

#2026-06-07 18:11:13 - __main__ - DEBUG - debug log statement
#2026-06-07 18:11:13 - __main__ - INFO - info log statement
#2026-06-07 18:11:13 - __main__ - WARNING - warning log statement
#2026-06-07 18:11:13 - __main__ - ERROR - error log statement
#2026-06-07 18:11:13 - __main__ - CRITICAL - critical log statement