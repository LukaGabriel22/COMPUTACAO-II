class CalculadoraException(Exception):
    pass


class Calculadora:
    def somar(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a + b

    def subtrair(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a - b

    def multiplicar(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        return a * b

    def dividir(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise CalculadoraException("Parâmetros não são números")
        if b == 0:
            raise CalculadoraException("Divisão por zero!")
        return a / b
