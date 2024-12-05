class Pet:

    all = []

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if self.check_pet_type(pet_type):
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
        else:
            raise TypeError('Pet type must be an instance of Pet Types')
    
    @classmethod
    def check_pet_type(cls, pet_type):
        return pet_type in cls.PET_TYPES

    
    
class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('Pet must be an instance of Pet class')
        pet.owner = self

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key = lambda pet: pet.name )