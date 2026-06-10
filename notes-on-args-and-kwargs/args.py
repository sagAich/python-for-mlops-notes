#variable length arguments
# *args:
# 1. when you do not know the exact number of arguments that will be passed to a function.
# 2. when you want to pass a list or a tuple as an argument to a function. Inside the function, args will still be a tuple,
#  regardless of whether you passed a list or a tuple.
def employee_details(*employee):
    print(f"type inside function: {type(employee)}")
    print(f"Content: {employee}")

employee_details_list = ["Sagar", "Aich", "Software Engineer"]
employee_details_tuple = ("Sagar", "Aich", "Software Engineer")
employee_details(*employee_details_list)
employee_details(*employee_details_tuple)
# for employee_details(*employee_details_list), the * operator unpacks the list into individual arguments: Sagar, Aich, Software Engineer
# Here, *employee collects all positional arguments into a tuple.
# So internally it becomes:
# employee = ("Sagar", "Aich", "Software Engineer")
# for employee_details(*employee_details_tuple), the * operator unpacks the tuple into individual arguments: Sagar, Aich, Software Engineer
# Here, *employee collects all positional arguments into a tuple.
# So internally it becomes:
# employee = ("Sagar", "Aich", "Software Engineer")
# If you want the function to receive the list itself

# Don't unpack it.
# def employee_details(employee):
#     print(type(employee))
#     print(employee)
#
# employee_details(employee_details_list)