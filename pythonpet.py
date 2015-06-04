__author__ = 'Luke Merrett'

from PetObjects.pet import Pet

myPet = None
console_options = None

def run_option(x):
    console_options[x]()

def wait():
    print("Waiting")

def console_loop():
    pets_status = myPet.get_pets_status()

    if pets_status.has_reached_its_lifespan:
        print('Your pet has died!')
        exit()

    print('\nPet status')
    print('----------\n')
    print(myPet.Age.current_age_string())
    print('Hungry: ' + ('Yes! Feed Me!' if pets_status.is_hungry else 'Not yet'))
    print('')
    print('What would you like to do:\n')
    print('1. Feed Pet')
    print('2. Wait')
    print('3. Exit')

    number_chosen = input('Choose a number (1,2,3): ')

    run_option(number_chosen)

# Entry Point
if __name__ == '__main__':
    print('Creating your pet')

    myPet = Pet()
    myPet.hatch()

    console_options = {
        '1': myPet.HungerLevel.feed_pet,
        '2': wait,
        '3': exit
    }

    print('Your pet has hatched; welcome it to the new world!')

    while(True):
        console_loop()

    exit()