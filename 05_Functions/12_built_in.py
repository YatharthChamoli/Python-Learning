def chai_flavour(flavour="masala"):
    """Returns the flavour of chai."""
    chai="ginger"
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)



def generate_bill(chai=0, samosa=0):
    """
    Generates total bill for chai and samosa.
    
    :param chai: Number of cups of chai
    :param samosa: Number of samosas
    :return: Total bill amount
    """
    total = chai * 10 + samosa * 20
    return total, "Thank you for visiting!"


print(generate_bill(2, 3))