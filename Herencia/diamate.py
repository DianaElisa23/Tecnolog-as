class A:
    def method(self):
        print("from A")

class B:
    def method(self):
        print("from B")

class C:
    def method(self):
        print("from C")

class D:
    def method(self):
        print("from D")

d = D()
print(D.mro())
d.method()