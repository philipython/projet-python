# 1. Une classe est un type de truc, sur lequel on peut définir des opérations.

class Dog():
    def __init__(self, age, color):
        self.age = age
        self.color = color
        self.is_alive = True

    def addition(self, x, y):
        return x + y



# use function addition



# Alternative
    
def addition(x,y):
    return x+y