class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) /
                             (other.real * other.real + other.imaginary * other.imaginary),
                             (self.imaginary * other.real - self.real * other.imaginary) /
                             (other.real * other.real + other.imaginary * other.imaginary))

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def get_real(self):
        return self.real

    def get_imaginary(self):
        return self.imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
