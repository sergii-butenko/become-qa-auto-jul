class MathOperations:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def check_parameters(self):
        if self.b == 0:
            raise Exception("Could not be used dut to devision operation")

    def devision(self):
        return self.a / self.b

    def multiply(self):
        return self.a * self.b

    def add(self):
        return self.a + self.b 
