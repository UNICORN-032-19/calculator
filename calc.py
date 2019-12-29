import re
from operations import Operation, BR1, BR2


class UnknownOperation(NotImplementedError):
    pass


class UnknownError(Exception):
    def __str__(self):

        return f"UnknownError{self.args}"


class Calculator():

    REGEXP_ALL = r"((\d{1,20}(\.|\,)\d{1,20})|(\d{1,20})|(\+|\-|\*|\^|\#|\/|\(|\)|\.))"

    def __init__(self, start_auto=True):
        self.operations = Operation.get_operations()
        if start_auto:
            self.start()

    def prepare_data(self, input_str):
        matches = re.finditer(self.REGEXP_ALL, input_str, re.MULTILINE)
        return [match.group() for match in matches]

    def get_data(self):
        """
        This function for getting data from user
        return: list of elements
        """
        input_str = input("Введите операцию: ")
        return self.prepare_data(input_str)

    def check_data(self, elements):  # проверяет исключения, все, чтобы не было ошибок
        if elements[0] in self.operations.keys() - [BR1, BR2]:  # проверяем
            raise UnknownError("Вычисление не может начинаться с операции")
        if elements[-1] in self.operations.keys() - [BR1, BR2]:
            raise UnknownError("Вычисление не может оканчиваться операцией")

        for element in elements:
            if isinstance(element, str) and element not in self.operations:
                raise UnknownOperation(element)

    def compress(self, elements, index):
        first = elements[index - 1]
        second = elements[index + 1]
        cls = self.operations.get(elements[index], None)
        operation = cls()

        left_finish = 0 if index == 1 else index - 1
        right_first = len(elements) if index == len(elements) - 2 else index + 2
        return (
            elements[:left_finish]
            + [operation.calculate(first, second)]
            + elements[right_first:]
        )

    def get_priority(self, elements):
        result = []
        for index, element in enumerate(elements):
            if not isinstance(element, (int, float)):
                result += [(index, self.operations.get(element).priority())]
        return sorted(result, key=lambda k: k[1])

    def calc(self, elements):
        for index, element in enumerate(elements):
            try:
                element = float(element.replace(",", "."))
            except ValueError:
                pass
            elements[index] = element
        self.check_data(elements)
        print(elements)

        while elements.count(")") > 0:
            end = elements.index(")")
            start = (end - 1) - list(reversed(elements[:end])).index("(")
            cutted = elements[start + 1 : end]
            while len(cutted) > 1:
                priority = self.get_priority(cutted)
                cutted = self.compress(cutted, priority[0][0])
            elements[start : end + 1] = cutted
            print(elements)

        while len(elements) > 1:
            priority = self.get_priority(elements)
            print(priority)
            elements = self.compress(elements, priority[0][0])
            print(elements)
        return elements[0]

    def start(self):
        print("Для выхода нажмите <Ctrl> - C")
        while True:
            try:
                elements = self.get_data()
            except KeyboardInterrupt:
                print("Завершение программы")
                break

            try:
                result = self.calc(elements)
                print(result)
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
            except UnknownOperation as err:
                print("UnknownOperation", err)  # определяем какая неизвестная операция
            except UnknownError:
                print("UnknownError!")
