def serve_chai():
    chai_type = "Masala Chai"
    print(f"Serving a cup of {chai_type}.")


chai_type = "Green Tea"
serve_chai()
print(f"Outside the function, chai_type is still: {chai_type}")


def chai_counter():
    chai_order = "lemon chai" # Enclosing scope
    def print_order():
        chai_order = "Ginger chai"
        print("Inner:", chai_order)
    print_order()    
    print("Outer:", chai_order)   

chai_order = "Tulsi" # Global scope
chai_counter()
print("Global:", chai_order)   