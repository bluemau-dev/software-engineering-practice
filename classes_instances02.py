class Weapon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def description(self):
        return "{} is a {} weapon.".format(self.name, self.type)
        
Shotgun = Weapon("SPAS-12", "Close-Range")
Baseball_Bat = Weapon("Metal Bat", "Close-Range")
Sniper = Weapon("Hunting Rifle", "Long-Range")

print(Shotgun.description())
print(Baseball_Bat.description())
print(Sniper.description())