import dojo_pets1

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__( self , first_name , last_name , treats , pet_food , pet ):
        self.firstname = first_name
        self.lastname = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = dojo_pets1.Pet()
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self): 
        self.pet.play()
        return(self)
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return(self)
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self): 
        self.pet.noise()
        return(self)
    
    def printPetAttri(self): 
        self.pet.printAttributes()
        return(self)



Joel = Ninja( "Joel" , "Schuster" , 5 , 2 , 1 )
Joel.walk().feed().bathe().printPetAttri()