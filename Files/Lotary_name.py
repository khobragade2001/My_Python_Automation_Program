import random

def select_random():
    ls = ["ashish", "rajiv", "sumit", "sahil", "ranga", "anand", "vipul", "pratik", "sagar", "rahul"]
    
    selection = random.choice(ls)
    return selection

selected = []
while len(selected) < 3:
    name = select_random()
    if name not in selected:
        selected.append(name)
        #print(name, end=", ")

print("Selected names:", ", ".join(selected))

        
