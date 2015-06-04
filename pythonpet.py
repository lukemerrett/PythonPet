__author__ = 'Luke Merrett'

from PetObjects.pet import Pet

if __name__ == '__main__':
    print('Creating your pet')

    myPet = Pet()
    myPet.hatch()

    print(myPet.Age.current_age_string())

    pets_status = myPet.get_pets_status()

    if pets_status.has_reached_its_lifespan:
        print("Your pet has died!")
        exit()

    if pets_status.is_hungry:
        print("Your pet is hungry, better feed them!")