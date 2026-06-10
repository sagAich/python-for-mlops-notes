def best_employee(*emplopyee):
    print(f"the best employee is: {emplopyee[0]}")
    # or we can also write: print("the best employee is: {}".format(emplopyee[0]))
    # or print("the best employee is: " + emplopyee[0])
best_employee("Sagar", "Amit", "Shyamal", "Satyarth")

def sum_num(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_num(1, 2, 3, 4, 5))