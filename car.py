
class Car:
    def __init__(self, parameterName, parameterBrand, parameterColor):
        self.name = parameterBrand
        self.brand = parameterName
        self.color = parameterColor

    def drive(self):
        print(f"The {self.color} {self.brand} {self.name} is driving.")

kiaMorning = Car("KIAMorning", "Kia", "Red")        
kiaMorning.drive()  

ferrari = Car("Ferrari", "Ferrari", "Yellow")
ferrari.drive()