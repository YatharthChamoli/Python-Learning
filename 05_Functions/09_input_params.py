# chai = "Ginger Chai"

# def prepare_chai(order):
#     print("Preparing your", order)

# prepare_chai(chai)
# print(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)    

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keyword

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Oolong", "Almond Milk", sweetness="High", foam="Light")    