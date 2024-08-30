""" Cat class """


class Cat:
    """Cat class"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.age = 0
        self.asleep = False

    def speak(self) -> str:
        """Cat speaks"""
        return "Meow"

    def aging(self) -> int:
        """Cat ages"""
        self.age += 1
        return self.age

    def sleep(self) -> bool:
        """Cat sleeps"""
        self.asleep = True
        return self.asleep
