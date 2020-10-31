class stu:

  def __init__(self, name, eng, math, sci, sst):
    self.name = name
    self.eng = eng
    self.math = math
    self.sci = sci
    self.sst= sst


a=stu("",78,56,95,34)
b=stu("",56,58,67,78)
c=stu("",98,78,67,56)
d=stu("",56,74,38,93)

a.name=input("Enter the name of student a")
b.name=input("Enter the name of student b")
c.name=input("Enter the name of student c")
d.name=input("Enter the name of student d")

print(vars(a))
print(vars(b))
print(vars(c))
print(vars(d))
