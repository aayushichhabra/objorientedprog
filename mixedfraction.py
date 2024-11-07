

class MixedFraction:
    def __init__(self, whole, numerator, denominator):
        if denominator == 0:
            print("Denominator cannot be zero.")
        if numerator >= denominator:
            whole += numerator // denominator
            numerator = numerator % denominator
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.whole} {self.numerator}/{self.denominator}"
    def to_improper(self):
        improper_numerator = self.whole * self.denominator + self.numerator
        return improper_numerator, self.denominator
    def print_improper(self):
        improper_numerator, improper_denominator = self.to_improper()
        print(f"Improper fraction: {improper_numerator}/{improper_denominator}")
    def __add__(self, other):
        num1, denom1 = self.to_improper()
        num2, denom2 = other.to_improper()
        common_denominator = denom1 * denom2
        num1 = num1 * denom2
        num2 = num2 * denom1
        result_numerator = num1 + num2
        return MixedFraction(0, result_numerator, common_denominator)
    def __sub__(self,other):
        num1, denom1= self.to_improper()
        num2, denom2=other.to_improper()
        common_denominator=denom1 * denom2
        num1 = num1 * denom2
        num2 = num2 * denom1
        result_numerator = num1 - num2
        return MixedFraction(0, result_numerator, common_denominator)

m1=MixedFraction(4,5,6)
m2=MixedFraction(1,2,3)
print(m1)
print(m2)
m1.print_improper()
m2.print_improper()
m3=m1+m2
print(m3)
m4=m1-m2
print(m4)
        
