class Pokemon:
    
    # Class variable: defined on the class and shared by Pokemon instances.
    overtime_pay = 1.5
    
    def __init__(self, name, type1, type2, pay):
        # Instance variables: initialized separately for each Pokemon object.
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.pay = pay
    
    def add_overtime(self):
        self.pay = self.pay + (self.pay * self.overtime_pay)
        
Slowbro = Pokemon("Slowbro", "Water", "Psychic", 20000)
Slowbro.add_overtime()

print(Slowbro.pay)
print(Slowbro.__dict__)
