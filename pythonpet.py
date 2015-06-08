__author__ = 'Luke Merrett'

from EnvironmentObjects.environment import Environment
from PetObjects.pet import Pet

console_options = None
environment = None
myPet = None

def run_option(x):
    if x in console_options:
        console_options[x]()
    else:
        print("You didn\'t enter an option")
        wait()

def wait():
    print("Waiting")

def console_loop():
    pets_status = myPet.get_pets_status()

    if pets_status.has_reached_its_lifespan:
        print('Your pet has died!')
        exit()

    print('\n%s\'s status' % myPet.Name)
    print('----------\n')
    print(myPet.Age.current_age_string())
    print('Hungry: ' + ('Yes! Feed Me!' if pets_status.is_hungry else 'Not yet'))
    print('Needs the Toilet: ' + ('Bursting!' if pets_status.needs_the_toilet else 'Nope'))
    print('Poop in the Cage: ' + environment.current_poop_level().__str__())
    print('')
    print('What would you like to do:\n')
    print('1. Feed Pet')
    print('2. Go to Toilet')
    print('3. Clean up the Poop')
    print('4. Wait')
    print('5. Exit')

    number_chosen = input('Choose a number (1,2,3 etc): ')

    run_option(number_chosen)

# Entry Point
if __name__ == '__main__':
    environment = Environment()
    myPet = Pet()

    print('What would you like to call your pet? ')
    pets_name = input('Name: ')

    myPet.hatch(environment, pets_name)

    console_options = {
        '1': myPet.HungerLevel.feed_pet,
        '2': myPet.Bladder.go_to_toilet,
        '3': environment.clean_up_poop,
        '4': wait,
        '5': exit
    }

    print('Your pet has hatched; welcome it to the new world!')

    while(True):
        console_loop()

    exit()