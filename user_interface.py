from tkinter import Tk, Frame, Label, Button
from calc import Calculator, UnknownOperation, UnknownError


class Main(Frame):
    formula = "0"

    def __init__(self, root):
        super().__init__(root)
        self.build()

    def build(self):
        self.calc = Calculator(start_auto=False)
        self.lbl_err = Label(
            text="",
            font=("Times New Roman", 21, "bold"),
            bg="#000", foreground="#FF0"
        )
        self.lbl_err.place(x=11, y=5)
        self.lbl = Label(
            text=self.formula,
            font=("Times New Roman", 21, "bold"),
            bg="#000", foreground="#FFF"
        )
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2",
        ]
        x = 10
        y = 100
        for btn in btns:
            command = lambda x=btn: self.command(x)
            Button(
                text=btn, bg="#FFF",
                font=("Times New Roman", 15), command=command
            ).place(
                x=x, y=y, width=115, height=79
            )
            x += 117
            if x > 400:
                x = 10
                y += 81

    def get_result(self, string):
        result = "0"
        error = ""
        elements = self.calc.prepare_data(string)
        try:
            result = self.calc.calc(elements)
        except ZeroDivisionError:
            error = "На ноль делить нельзя!"
        except UnknownOperation as err:
            error = 'UnknownOperation'
        except UnknownError:
            error = 'UnknownError!'
        return str(result), str(error)

    def command(self, symbol):
        need_update = True
        if symbol == "C":
            self.formula = "0"
        elif symbol == "DEL":
            self.formula = self.formula[0:-1]
        elif symbol == "=":
            result, error = self.get_result(self.formula)
            if error:
                self.lbl_err.configure(text=error)
                need_update = False
            else:
                self.formula = result


        elif symbol == "X^2":
            error = ""
            try:
                float(self.formula)
            except ValueError:
                result1, error = self.get_result(self.formula)

            try:
                if error:
                    raise ValueError(error)

                result, error = self.get_result(result1 + '^2')
                if error:
                    raise ValueError(error)
                self.formula = result
            except ValueError as error:
                self.lbl_err.configure(text=str(error))
                need_update = False
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += symbol
        if need_update:
            self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)
        self.lbl_err.configure(text="")


if __name__ == "__main__":
    root = Tk()
    root["bg"] = "#000"
    root.title("Калькулятор")
    root.geometry("485x550+200+200")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
