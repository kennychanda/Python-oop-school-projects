class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def val(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def disp(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def area(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is ", area)
    def peri(self):
        a,b,c= self.sides
        peri=a+b+c
        print("Perimeter is ", peri)

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)

    def area(self):
        a= self.sides
        area = a[0]**2
        print("The area of the square is", area)
    def peri(self):
        a= self.sides
        peri=a[0]*4
        print("Perimeter is ", peri)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)

    def area(self):
        a= self.sides
        area = a[0]*a[1]
        print("The area of the rectangle is", area)
    def peri(self):
        a= self.sides
        peri=(a[0]+a[1])*2
        print("Perimeter is ", peri)

class Hexagon(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)

    def area(self):
        a= self.sides
        area =(((3**0.5)*(a[0]**2))/(4))*6
        print("The area of the regular hexagon is", area)
    def peri(self):
        a= self.sides
        peri=a[0]*6
        print("Perimeter is ", peri)


print("Triangle lengths 3")
x=Triangle()
x.val()
x.disp()
x.area()
x.peri()
print("Square values 1")
y=Square()
y.val()
y.disp()
y.area()
y.peri()
print("Rectangle values 2")
z=Rectangle()
z.val()
z.disp()
z.area()
z.peri()
print("Regular Hexagon values 1")
w=Hexagon()
w.val()
w.disp()
w.area()
w.peri()
