def main():
    qty = None
    cost = None
def fetch_quantity():
    try:
        """
        Returns a number, any number
        """
        ...
        return ...
    except Exception as e:
        print(e)
        exit()
def fetch_cost():
    try:
        """
        Returns a number, any number
        """
        ...
        return ...
    except:
        pass
        

def compute_cost_per_quantity():
    qty = fetch_quantity()
    cost = fetch_cost()
    try:
        cost_per_quantity = cost/qty
    except Exception as e:
        print(e)
        exit()
        
        
    return cost_per_quantity

cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)

