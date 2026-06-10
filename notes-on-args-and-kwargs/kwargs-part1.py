# * - wild card
# ** - double wild card
def func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
func(1, 2, 3, name="Sagar", age=30)
# In this example, *args collects the positional arguments (1, 2, 3) into a tuple, 
# and **kwargs collects the keyword arguments (name="Sagar", age=30) into a dictionary.