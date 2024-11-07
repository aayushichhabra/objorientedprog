class SpecialPlus:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add_and_multiply(self):
        return (self.a + self.b) * 2
    def __repr__(self):
        return f"SpecialPlus(a={self.a}, b={self.b})"
    def add_and_divide(self):
        return (self.a + self.b)/2
    def __add__(self, other):
        return SpecialPlus(self.a+other.a,self.b+other.b)
    def __sub__(self, other):
        return SpecialPlus(self.a-other.a,self.b-other.b)
    def __repr__(self):
        return f"SpecialPlus(a={self.a}, b={self.b})"
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    def __neg__(self):
        return SpecialPlus(-self.a, -self.b)
    


q1=SpecialPlus(7,4)
q2=SpecialPlus(9,6)
print(q1)
print(q2)
print(q1.add_and_multiply())
print(q1.add_and_divide())
q3=q1+q2
print(q3)
print(q3.add_and_multiply())
q4=q2-q1
print(q4)
print(q4.add_and_multiply())
negq1=-q1
negq2=-q2
print(negq1)
print(negq2)

