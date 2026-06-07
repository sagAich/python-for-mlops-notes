#Following are the logging levels:

#DEBUG - Detailed information, typically of interest only when diagnosing problems.
#INFO - Confirmation that things are working as expected.
#WARNING - An indication that something unexpected happened, or indicative of some problem 
# in the near future (e.g. ‘disk space low’). The software is still working as expected. this is the default logging level.
#ERROR - Due to a more serious problem, the software has not been able to perform some function.
#CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

# If we set the logging level to WARNING, then only WARNING, ERROR and CRITICAL messages will be logged.
# If we set the logging level to ERROR, then only ERROR and CRITICAL messages will be logged.
# If we set the logging level to CRITICAL, then only CRITICAL messages will be logged.
# If we set the logging level to DEBUG, then all messages will be logged.

#following is the code to demonstrate the logging levels: 
# to show that if we do not define logging.basicConfig(level=logging.DEBUG), to set the logging level to DEBUG,
# then only WARNING, ERROR and CRITICAL messages will be logged by default.

import logging
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

#WARNING:root:sum and Product: 8 15 
#ERROR:root:sum and Product: 8 15
#CRITICAL:root:sum and Product: 8 15