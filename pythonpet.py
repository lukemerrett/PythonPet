__author__ = 'Luke Merrett'

from PetObjects.pet import Pet

if __name__ == '__main__':
    print('Creating your pet')

    myPet = Pet()
    myPet.hatch()

    print(myPet.current_age_string())

    pets_status = myPet.get_pets_status()

    print(pets_status.has_reached_its_lifespan)