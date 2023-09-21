import csv
import re


class BasicException(Exception):
    pass


class BasicExceptionMissingItemDatabase(BasicException):
    def __str__(self):
        return 'Такой предмет отсутствует'


class BasicExceptionErrorEnteringFullName(BasicException):
    def __str__(self):
        return 'Нужно ввести Фамилию Имя Отчество полностью'


class BasicExceptionRangeError(BasicException):
    def __init__(self, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value

    def __str__(self):
        return f'Значение должна быть {self.__min_value}-{self.__max_value}'


class BasicExceptionValueWithNumbersOrLowerCase(BasicException):
    def __str__(self):
        return 'Должно содержать только буквы и начинаться с большой буквы.'


class CorrectName:
    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        pattern = r'\d'
        if bool(re.search(pattern, value)) or not value.istitle():
            raise BasicExceptionValueWithNumbersOrLowerCase


class CorrectNum:
    def __init__(self, min_value: int, max_value: int):
        self.__min_value = min_value
        self.__max_value = max_value

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not self.__min_value <= value <= self.__max_value:
            raise BasicExceptionRangeError(self.__min_value, self.__max_value)


class Student:
    __name = CorrectName()
    __surname = CorrectName()
    __patronymic = CorrectName()
    __grade = CorrectNum(min_value=2, max_value=5)
    __points = CorrectNum(min_value=0, max_value=100)

    def __init__(self, surname: str, name: str, patronymic: str):
        try:
            self.__surname: str = surname
            self.__name: str = name
            self.__patronymic: str = patronymic
        except ValueError:
            raise BasicExceptionErrorEnteringFullName
        self.__school_items: list[str] = self.__load_items()
        self.__test_grade_book: dict[str, list[int]] = {lesson: [] for lesson in self.__school_items}
        self.__subject_grade_book: dict[str, list[int]] = {lesson: [] for lesson in self.__school_items}
        self.__average_test_score: dict[str, int] = {}
        self.__average_score_all_subjects: int = 0

    def rate(self, name_item: str, grade: int):
        if name_item in self.__subject_grade_book:
            self.__grade = grade
            self.__subject_grade_book[name_item].append(self.__grade)
        else:
            raise BasicExceptionMissingItemDatabase

    def give_points(self, name_item: str, grade: int):
        if name_item in self.__test_grade_book:
            self.__points = grade
            self.__test_grade_book[name_item].append(self.__points)
        else:
            raise BasicExceptionMissingItemDatabase

    def __get_average_test_score(self):
        self.__average_test_score = {}
        for key, item in self.__test_grade_book.items():
            if len(item) > 0:
                self.__average_test_score[key] = round(sum(item) / len(item), 1)
            else:
                self.__average_test_score[key] = None

    def __get_average_score_for_all_subjects(self):
        average_score_all_subjects = 0
        number_ratings: int = 0

        for key, item in self.__subject_grade_book.items():
            if len(item) > 0:
                number_ratings += len(item)
                average_score_all_subjects += sum(item)

        if number_ratings > 0:
            self.__average_score_all_subjects = int(average_score_all_subjects / number_ratings)

    def __load_items(self):
        with open('school_items.csv', "r", encoding='utf-8') as csv_file:
            csv_reader = list(csv.reader(csv_file))[0]
            return csv_reader

    def __str__(self):
        self.__get_average_test_score()
        self.__get_average_score_for_all_subjects()
        return (f'Ученик: {self.__surname} {self.__name} {self.__patronymic}\n'
                f'Средняя оценка по всем предметам: {self.__average_score_all_subjects}\n'
                f'Средний балл по тестам: {self.__average_test_score}')


if __name__ == '__main__':
    petrov = Student(surname='Попов', name='Антон', patronymic='Викторович')
    petrov.rate(name_item='математика', grade=5)
    petrov.rate(name_item='русский', grade=5)
    petrov.rate(name_item='литература', grade=5)
    petrov.rate(name_item='химия', grade=3)
    petrov.rate(name_item='физика', grade=2)
    petrov.give_points(name_item='математика', grade=100)
    petrov.give_points(name_item='математика', grade=10)
    petrov.give_points(name_item='русский', grade=33)
    petrov.give_points(name_item='химия', grade=10)
    petrov.give_points(name_item='химия', grade=50)
    ivanov = Student(surname='Иванов', name='Иван', patronymic='Иванович')
    ivanov.rate(name_item='математика', grade=3)
    ivanov.rate(name_item='русский', grade=3)
    ivanov.rate(name_item='литература', grade=3)
    ivanov.rate(name_item='химия', grade=2)
    ivanov.rate(name_item='физика', grade=2)
    ivanov.give_points(name_item='математика', grade=27)
    ivanov.give_points(name_item='математика', grade=10)
    ivanov.give_points(name_item='математика', grade=31)
    ivanov.give_points(name_item='физика', grade=10)
    ivanov.give_points(name_item='химия', grade=50)
    print(petrov)
    print(ivanov)
