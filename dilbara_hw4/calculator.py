class Calculator:
    def plus(self, a, b, *args):
        z = 0
        for num in args:
            z += num
        print(a, "+", b,'+',z,"=",  a + b + z)
    def minus(self,a ,b, *args):
        z = 0
        for num in args:
            z += num
        print(a, "-", b,'-',z,"=", a - b)
    def devide(self,a,b, *args):
        z = 0
        for num in args:
            z += num
        print(a, "/", b,'/', z, "=", a // b)
    def mult(self,a,b, *args):
        z = 0
        for num in args:
            z += num
        print(a, "*", b, '*', z, "=", a * b)
