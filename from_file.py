from calc import Calculator, UnknownOperation, UnknownError

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"


def get_data():
    with open(INPUT_FILENAME) as file:
        data = file.readlines()
    data = [x.strip() for x in data]
    return data


def write_data(output_data):
    output_data = [str(x) + "\n" for x in output_data]
    print(output_data)
    with open(OUTPUT_FILENAME, "w") as out_file:
        out_file.writelines(output_data)


if __name__ == "__main__":
    CALC = Calculator(start_auto=False)
    DATA = get_data()
    RESULTS = []
    for line in DATA:
        elements = CALC.prepare_data(line)
        try:
            result = CALC.calc(elements)
            RESULTS.append(result)
        except ZeroDivisionError:
            RESULTS.append("На ноль делить нельзя!")
        except UnknownOperation as err:
            RESULTS.append("UnknownOperation")  # определяем какая неизвестная операция
        except UnknownError:
            RESULTS.append("UnknownError!")

    write_data(RESULTS)
    print(RESULTS)
