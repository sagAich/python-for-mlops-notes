#variable length arguments
# *args:
# 1. when you do not know the exact number of arguments that will be passed to a function.
# 2. when you want to pass a list or a tuple as an argument to a function.
def employee_details(*employee):
    print(f"type inside function: {type(employee)}")
    print(f"Content: {employee}")

employee_details_list = ["Sagar", "Aich", "Software Engineer"]
employee_details_tuple = ("Sagar", "Aich", "Software Engineer")
employee_details(*employee_details_list)
employee_details(*employee_details_tuple)
