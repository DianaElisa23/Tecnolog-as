#include <iostream>

class Animal {
public:
    virtual ~Animal() = default;
    void respirar() const { std::cout << "Respirando!\n"; }
};

struct Perro : Animal {
    void ladrar() const { std::cout << "Woof\n"; }
};

struct Gato : Animal {
    void maullar() const { std::cout << "Miau\n"; }
};

int main() {
    Perro p;
    Gato g;

    p.respirar();
    p.ladrar();

    g.respirar();
    g.maullar();

    return 0;
}