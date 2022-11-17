class objectss:
    x=10
    y=10
class functions:
    def test_add(self,x,y):
        return x + y
    def test_subtract(self,x,y):
        return x - y
    def test_multiply(self,x,y):
        return x * y
    

class TestMath:
    o1 = objectss()
    o2 = functions()
    
    print(o1.x)
    print(o1.y)
    print(o2.test_add(o1.x,o1.y))
    print(o2.test_subtract(o1.x,o1.y))
    print(o2.test_multiply(o1.x,o1.y))

    

    
    
    
    