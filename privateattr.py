class stu:

    def __init__(self, name, age, number,address,det):
        self.value={"name":name,"age":age,"number":number,"address":address,"det":det} 

    def disp(self):
        print(self.value)

# Method 2
    def _disp(self):
        print(self.value)

class details:
    def __init__(self,value):
        self.val1=stu("a",18,56,95,34)
        self.val2=stu("b",16,58,67,78)
# Method 1
        self._val3=stu("c",18,78,67,56)
        self._val4=stu("d",16,74,38,93)
        self._val5=stu("e",17,12,23,34)

# Method 3
class _details:
    def __init__(self,value):
        self.val3=stu("ch",1,1,1,1)
        self.val4=stu("ch",1,1,1,1)
        self.val5=stu("ch",1,1,1,1)

val=details(stu)
val1=_details(stu)

print("output for method 1")
val.val1.disp()
val.val2.disp()
val._val3.disp()
val._val4.disp()
val._val5.disp()
print("output for method 2")
val.val1._disp()
val.val2._disp()
val._val3._disp()
val._val4._disp()
val._val5._disp()
print("output for method 3")
val1.val3.disp()
val1.val4.disp()
val1.val5.disp()
