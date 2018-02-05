class Person:

    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def get_name(self) -> str:
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def __str__(self) -> str:
        return "Person[name: " + self.__name + ", address: " + self.address + "]"
