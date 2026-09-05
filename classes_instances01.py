# Python Object-Oriented Programming

class Superhero:
    
    def __init__(self, first, last, power):
        self.first = first
        self.last = last
        self.power = power
        
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
Bluemau = Superhero("Blue", "Mau", "Energy")
YodTheSuper = Superhero("Yod", "Super", "Space")

class Villain:
    def __init__(self, first, last, power):
        self.first = first
        self.last = last
        self.power = power
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)

# Superhero Output
# Both Print the Same
print(Bluemau.full_name()) # Uses Self to run the Instance of the Class
print(Superhero.full_name(Bluemau)) # Needs an Argument in this case it is an instance of the

# Villain Output
Moistness = Villain("Moist", "Ness", "Life")
print(Moistness.full_name())