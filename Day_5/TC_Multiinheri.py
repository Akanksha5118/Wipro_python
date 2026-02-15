class A:
    def showA(self):
        print("A from class A")

class B:
    def showB(self):
        print("B")

class C(A, B):
    pass

c = C()
c.showA()
c.showB()



