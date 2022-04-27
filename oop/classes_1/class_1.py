'''A class'''

class Dog:
    def __init__(self, name: str, race: str, age: int):
        self.name: str = name
        self.race: str = race
        self.age : int = age

    def __str__(self) -> str:
        return f"{self.name} is a {self.race} and is {self.age} year old"

if __name__ == "__main__":
    fosc: Dog = Dog("Fosc", "Mixed", 5)
    leia: Dog = Dog("Leia", "Border Collie", 2)

    print(f"{fosc}\n{leia}")
