#This code is to show that how we can create the timestamp in logs inside a file.
import logging

logging.basicConfig( filename="app.log", level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
# %(asctime)s will add the timestamp to the log message, 
# %(levelname)s will add the logging level to the log message,
# %(message)s will add the log message to the log message. 
#  for better understanding of format, refer to the output.


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
#2023-10-10 12:00:00,000 - DEBUG - sum and Product: 8 15
#2023-10-10 12:00:00,000 - INFO - sum and Product: 8 15
#2023-10-10 12:00:00,000 - WARNING - sum and Product: 8 15
#2023-10-10 12:00:00,000 - ERROR - sum and Product: 8 15
#2023-10-10 12:00:00,000 - CRITICAL - sum and Product: 8 15
