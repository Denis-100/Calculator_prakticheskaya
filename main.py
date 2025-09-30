# Класс калькулятор
class Calculator:
    # Инициилизация базовых значений 1 1
    def __init__(self):
        # Базовые значения
        self.a = 1
        self.b = 1

        # Ответ
        self.otvet = 0

        # Выбор операции
        self.choise = None

        #Получение данных пользователя при создании объекта класса
        self.get_input()
    
    # Получение данных от пользователя
    def get_input(self):
        self.a = int(input("Введите 1-е число: "))
        self.b = int(input("Введите 2-е число: "))
        self.choise = input("Выберите операция: + = * /: ")
        self.start_calc()
    
    # Запуск калькулятора
    def start_calc(self):
        match self.choise:
            case "+":
                self.otvet = self.summ()
            case "-":
                self.otvet = self.razn()
            case "*":
                self.otvet = self.proiz()
            case "/":
                self.otvet = self.delenie()
        self.print_otvet()
    
    # Функция сложения
    def summ(self):
        return self.a + self.b

    # Функция вычитания
    def razn(self):
        return self.a - self.b
    
    # Функция умножения
    def proiz(self):
        return self.a * self.b
    
    # Функция деления
    def delenie(self):
        if self.b <= 0:
            print("На 0 делить нельзя")
            self.get_input()
        else:
            return self.a / self.b
    
    # Функция вывода ответа
    def print_otvet(self):
        print(f"Ответ: {self.otvet}")
    
calc = Calculator()
