import math

class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            print("Denominator cannot be zero.")
        
        self.num = num
        self.denom = denom
    def __str__(self):
        return f"{self.num}/{self.denom}"

f1 = Fraction(3, 4)
f2 = Fraction(2, 5)
print(f1)
print(f2)
