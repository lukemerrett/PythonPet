__author__ = 'Luke Merrett'

from pet import Pet

if __name__ == '__main__':
    print('Creating your pet')

    myPet = Pet()
    myPet.hatch()

    print(myPet.current_age_string())