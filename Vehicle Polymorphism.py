class BMW:
    
    def fuel_type(self):
        print ("BMW m5 Fuel Type is Petrol")
    def max_speed(self):
        print ("BMW m5 Max Speed is 250 kmh")
    def mileage(self):
        print ("BMW mileage is 9 kmpl")
        
class Mclaren:
    
    def fuel_type(self):
        print ("Mclaren 720s Fuel Type is Petrol")
    def max_speed(self):
        print ("Mclaren 720s Max Speed is 312 kmh")
    def mileage(self):
        print ("Mclaren 720s mileage is 5 kmpl")
        
class  Koenigsegg:
    
    def fuel_type(self):
        print ("Koenigsegg jesko Fuel Type is Petrol")
    def max_speed(self):
        print ("Koenigsegg jesko Max Speed is 412 kmh")
    def mileage(self):
        print ("Koenigsegg jesko mileage is 3 kmpl")
        
class  Lamborghini:
    
    def fuel_type(self):
        print  ("Lamborghini huracan Fuel Type is Petrol")
    def max_speed(self):
        print ("Lamborghini huracan Max Speed is 325 kmh")
    def mileage(self):
        print ("Lamborghini huracan mileage is 11 kmpl")

class  Land_Rover:
    
       
    def fuel_type(self):
        print  ("Range Rover Fuel Type is Octane")
    def max_speed(self):
        print ("Range Rover Max Speed is 234 kmh")
    def mileage(self):
        print ("Range Rover mileage is 13 kmpl")
        
bmw = BMW()
mclaren = Mclaren()
koenigsegg = Koenigsegg()
lamborghini = Lamborghini()
landrover = Land_Rover

for car in (bmw,mclaren,koenigsegg,lamborghini,landrover):
    
    car.fuel_type()
    car.max_speed()
    car.mileage()



    