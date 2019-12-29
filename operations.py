SUM = "+"
DEC = "-"
MUL = "*"
DIV = "/"
EXP = "^"
ROT = "#"
BR1 = "("
BR2 = ")"
END = "."


class Operation():
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

    def calculate(self, *args, **kwargs):
        arg1 = args[0]
        arg2 = args[1]
        return arg1 ** arg2


class RootOfOperation(Operation):
    __priority = 1
    __identificator = [ROT]

    def calculate(self, *args, **kwargs):
        arg1 = args[0]
        arg2 = args[1]

        return arg1 ** (1 / arg2)


class BracketOperation(Operation):
    __priority = 1
    __identificator = [BR1, BR2]

    def calculate(self, *args, **kwargs):
        return


if __name__ == "__main__":
    import traceback

    TEST_CASES = [
        {"cls_tc": SumOperation, "args": [1, 2, 3], "expected_result": 6},
        {"cls_tc": SumOperation, "args": [2, 3], "expected_result": 5},
        {"cls_tc": DecOperation, "args": [1, 2, 3], "expected_result": -4},
        {"cls_tc": MultiplicationOperation, "args": [8, 8, 2, 2], "expected_result": 256},
        {"cls_tc": DivisionOperation, "args": [16, 4, 2, 1], "expected_result": 2},
        {"cls_tc": ExponentialOperation, "args": [8, 2], "expected_result": 64},
        {"cls_tc": RootOfOperation, "args": [16, 2], "expected_result": 4},
        {"cls_tc": BracketOperation, "args": [16, 2], "expected_result": None},
    ]

    GREEN = 0
    RED = 0
    for test_case in TEST_CASES:
        cls_tc = test_case["cls_tc"]
        op = cls_tc()
        expected_result = test_case["expected_result"]
        result_tc = op.calculate(*test_case["args"])
        try:
            assert (
                result_tc == expected_result
            ), f"calculate returns: {result_tc}, expected: {expected_result}, \
            operation is {cls_tc.__name__}"
            GREEN += 1
        except AssertionError:
            RED += 1
            print(traceback.format_exc())
    all_messages = GREEN + RED
    print(f"Run {all_messages} tests, {GREEN} passed, {RED} failed")
