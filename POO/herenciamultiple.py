class A():
    def mensaje(self):
        print("Esta es la clase A")

    def primera(self):
        print("estas en la Clase A")

class B():
    def mensaje(self):
        print("Esta es la clase B")
    def segunda(self):
        print("estas en la Clase B")

class C(B,A):
    pass

c=C()
c.primera()
c.segunda()


