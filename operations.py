SUM = "+"
DEC = "-"
MUL = "*"
DIV = "/"
EXP = "^"
ROT = "#"
BR1 = "("
BR2 = ")"
END = "."




class Operation(object):
    __priority = 0
    __identificator = None


    def calculate(self, *args, **kwargs):
        raise NotImplementedError


    @classmethod
    def get_operations(cls):
        return {
            SUM: SumOperation,
            DEC: DecOperation,
            MUL: MultiplicationOperation,
            DIV: DivisionOperation,
            EXP: ExponentialOperation,
            ROT: RootOfOperation,
            BR1: BracketOperation,
            BR2: BracketOperation,
        }


    @classmethod
    def priority(cls):
        return cls.__priority




class SumOperation(Operation):
    __priority = 3
    __identificator = [SUM]


    def calculate(self, *args, **kwargs):
        return sum(args)




class DecOperation(Operation):
    __priority = 3
    __identificator = [DEC]


    def calculate(self, *args, **kwargs):
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result




class MultiplicationOperation(Operation):
    __priority = 2
    __identificator = [MUL]


    def calculate(self, *args, **kwargs):
        result = args[0]
        for arg in args[1:]:
            result *= arg
        return result




class DivisionOperation(Operation):
    __priority = 2
    __identificator = [DIV]


    def calculate(self, *args, **kwargs):
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result




class ExponentialOperation(Operation):
    __priority = 1
    __identificator = [EXP]


    def calculate(self, a, n):
        return a ** n




class RootOfOperation(Operation):
    __priority = 1
    __identificator = [ROT]


    def calculate(self, a, n):
        return a ** (1 / n)




class BracketOperation(Operation):
    __priority = 1
    __identificator = [BR1, BR2]


    def calculate(self, *args, **kwargs):
        return




if __name__ == "__main__":
    import traceback


    TEST_CASES = [
        {"cls": SumOperation, "args": [1, 2, 3], "expected_result": 6},
        {"cls": SumOperation, "args": [2, 3], "expected_result": 5},
        {"cls": DecOperation, "args": [1, 2, 3], "expected_result": -4},
        {"cls": MultiplicationOperation, "args": [8, 8, 2, 2], "expected_result": 256},
        {"cls": DivisionOperation, "args": [16, 4, 2, 1], "expected_result": 2},
        {"cls": ExponentialOperation, "args": [8, 2], "expected_result": 64},
        {"cls": RootOfOperation, "args": [16, 2], "expected_result": 4},
        {"cls": BracketOperation, "args": [16, 2], "expected_result": None},
    ]


    green = 0
    red = 0
    for test_case in TEST_CASES:
        cls = test_case["cls"]
        op = cls()
        expected_result = test_case["expected_result"]
        result = op.calculate(*test_case["args"])
        try:
            assert result == expected_result, f"calculate returns: {result}, expected: {expected_result}, operation is {cls.__name__}"
            green += 1
        except AssertionError:
            red += 1
            print(traceback.format_exc())
    all = green + red
    print(f"Run {all} tests, {green} passed, {red} failed")

