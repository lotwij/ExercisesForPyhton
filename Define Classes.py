class pet_animal:

    def __init__(self, name, kind_of_pet, age, temperament, trained):
        self.name = name
        self.kind_of_pet = kind_of_pet
        self.age = age
        self.temperament = temperament
        self.trained = trained

Jacky = pet_animal("Jacky", "dog", 15, "Fierce", True)
print(Jacky.age)