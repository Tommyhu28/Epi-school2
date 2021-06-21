class Triangle():
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        semi_p = (self.a+self.b+self.c)/2
        ans = (semi_p*(semi_p-self.a)*(semi_p-self.b)*(semi_p-self.c))**0.5
        return ans
    
    def perimeter(self):
        return self.a+self.b+self.c
    
    def scale(self, factor):
        return Triangle(factor*self.a,factor*self.b,factor*self.c)
    
    def is_valid(self):
        return (self.a+self.b > self.c and self.a+self.c > self.b and self.b+self.c > self.a)
    
    def is_right(self):
        hyp = max(self.a,self.b,self.c)
        if (hyp == self.a):
            return (hyp**2 == self.b**2 + self.c**2)
        if (hyp == self.b):
            return (hyp**2 == self.a**2 + self.c**2)
        if (hyp == self.c):
            return (hyp**2 == self.a**2 + self.b**2)

tri = Triangle(3,4,5)
print("Area = %d" % tri.area())
print("Perimeter = %d" %tri.perimeter())
print("Valid triangle?", tri.is_valid())
print("Right triangle?",tri.is_right())

new_tri = tri.scale(2)
print("Area = %d" % new_tri.area())
print("Perimeter = %d" % new_tri.perimeter())
print("Valid triangle?", new_tri.is_valid())
print("Right triangle?",new_tri.is_right())
