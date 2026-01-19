# def make_chai():
#     # return "Here is your masala chai!"
#     print("Here is your masala chai!")

# return_value = make_chai()

# print(return_value)

def idel_chaiwala():
    pass

print(idel_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "We are out of chai!"
    return "Chai is available."
    print("Chai")

print(chai_status(0))
print(chai_status(5))    


def chai_report():
    return 100 , 20 , 10 # total, sold, left

total, sold, left = chai_report()
print("Total:", total)
print("Sold:", sold)
