class House():
    def __init__(self, location, owner, price, room):
        self.location = location
        self.owner = owner
        self.price = price
        self.room = room


house_owner_one = House("Westlands", "Precious", "6.5M", "8 bedrooms")
print(house_owner_one.location)
print(house_owner_one.owner)
print(house_owner_one.price)
print(house_owner_one.room)

print("----------------End of house_owner_one-------------------")
house_owner_two = House("Ngara", "Kadish", "7M", "6 bedrooms")
print(house_owner_two.location)
print(house_owner_two.owner)
print(house_owner_two.price)
print(house_owner_two.room)