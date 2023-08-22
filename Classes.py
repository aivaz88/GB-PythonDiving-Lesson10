class Animal:
    def __init__(self, name: str, age: int, **_):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Type":*:0}{type(self).__name__}'
                f'\n{"Name:":0}{self.name}'
                f'\n{"Age:":0}{self.age} years')

class Mammal(Animal):
    def __init__(self, name: str, age: int, hair: str, voice: str, **_):
        super().__init__(name, age)
        self.hair = hair
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Hair:":0}{self.hair}'
                f'\n{"Voice:":0}{self.voice}'
                )

class Bird(Animal):
    def __init__(self, name: str, age: int, color: str, voice: str, **_):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":0}{self.color}'
                f'\n{"Voice:":0}{self.voice}'
                )

class Fish(Animal):
    def __init__(self, name: str, age: int, color: str, **_):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Color:":0}{self.color}'
                )