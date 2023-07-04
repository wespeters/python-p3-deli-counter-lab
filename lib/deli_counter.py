def line(customers):
    if not customers:
        print("The line is currently empty.")
    else:
        line_info = "The line is currently: "
        line_info += ' '.join(f"{i+1}. {name}" for i, name in enumerate(customers))
        print(line_info)

def take_a_number(customers, name):
    customers.append(name)
    print(f"Welcome, {name}. You are number {len(customers)} in line.")

def now_serving(customers):
    if not customers:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {customers.pop(0)}.")
