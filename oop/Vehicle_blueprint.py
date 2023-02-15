class Vehicle() :
    def __init__(self, owner, price, model, colour):
        self.owner = owner
        self.price = price
        self.model = model
        self.colour = colour

car_owner_one = Vehicle("Samantha", "10M", "G-class mercedes", "black")
print(car_owner_one.owner)
print(car_owner_one.price)
print(car_owner_one.model)
print(car_owner_one.colour)

print("-------End of car_owner_one------------")

car_owner_two = Vehicle("Sandy", "12M", "Mercedes C-200", "rose gold")
print(car_owner_two.owner)
print(car_owner_two.price)
print(car_owner_two.model)
print(car_owner_two.colour)

print("-------End of car_owner_two----------")

car_owner_three = Vehicle("Ndichu", "8M", "Jeep 350", "silver")
print(car_owner_three.owner)
print(car_owner_three.price)
print(car_owner_three.model)
print(car_owner_three.colour)

print("-------End of car_owner_three----------")