from element.person import Person


class SchoolList(object):

    __instance = None

    class __School(object):

        def __init__(self):
            self.__list = []

        def add(self, person: Person) -> bool:
            self.__list.append(person)
            return True

        def get(self, index) -> int:
            if 0 > index > len(self.__list):
                return -1

            return self.__list[index]

        def get_iterator(self):
            return SchoolList.SchoolIterator(self.__list)

        def size(self):
            return len(self.__list)

    class SchoolIterator(object):

        def __init__(self, school_list):
            self.__input_list = school_list
            self.__current = -1

        def has_next(self):
            return self.__current + 1 < len(self.__input_list)

        def next(self):
            self.__current += 1
            return self.__input_list[self.__current]

    def __init__(self):
        self.get_list()

    @classmethod
    def get_list(cls):
        if SchoolList.__instance is None:
            SchoolList.__instance = cls.__School()
        return SchoolList.__instance
