from Classes import *

class Fabric:

    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal]:
        try:
            animal = super().__new__(animal_type)
            animal.__init__(*args, **kwargs)
            return animal
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver', 1000)

def main():
    dog = Fabric(Mammal, name='Fibo', age=5, voice='Woof!', hair='Pale, long')
    fish = Fabric(Fish, name='Vanda', age=1, color='Rainbow')
    bird = Fabric(Bird, name='Carl', age=8, color='Black', voice='CRAW!')
    undentified = Fabric('Non-type', name='Fail_Tester', age=100, color='Green', voice='Boo', hair='blonde')

    print(dog.get_info(), '\n')
    print(fish.get_info(), '\n')
    print(bird.get_info(), '\n')
    print(undentified.get_info(), '\n')

if __name__ = '__main__':
    main()