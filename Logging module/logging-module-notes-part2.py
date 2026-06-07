#This code is to show that how we can create the logs inside a file.
import logging

logging.basicConfig( filename="app.log", level=logging.DEBUG, filemode='w') # by keeping filemode='w', 
# we can overwrite the existing log file, if we do not use it, then the logs will be appended to the existing log file.
# now if i were to create a separate directory for the logs, outside the current directory,
# then we can specify the path of the log file as well, for example: filename="..\\logs\\app.log"

class demologging:
    def add_numbers(self, a, b):
        return a + b
    def multiply_numbers(self, a, b):
        return a * b
dl = demologging()
sum_result = dl.add_numbers(5, 3)
product_result = dl.multiply_numbers(5, 3)

logging.debug("sum and Product: {} {}".format(sum_result, product_result))
logging.info("sum and Product: {} {}".format(sum_result, product_result))
logging.warning("sum and Product: {} {}".format(sum_result, product_result))
logging.error("sum and Product: {} {}".format(sum_result, product_result))
logging.critical("sum and Product: {} {}".format(sum_result, product_result))

#output:
# the logs will be written to the app.log file in the same directory where this code is executed. The content of the app.log file will be:
#DEBUG:root:sum and Product: 8 15
#INFO:root:sum and Product: 8 15
#WARNING:root:sum and Product: 8 15
#ERROR:root:sum and Product: 8 15
#CRITICAL:root:sum and Product: 8 15
