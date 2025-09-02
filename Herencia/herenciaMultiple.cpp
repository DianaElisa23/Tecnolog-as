#include <iostream>

class Volador {
    public:
    virtual ~Volador() = default;
    virtual void volar();
};

class Nadador {
    public:
    virtual ~Nadador() = default;
    virtual void nadar();
};

class Pato : public Volador, public Nadador {
    public:
    void volar() const { std::cout << "El pato vuela\n";}
    void nadar() const { std::cout << "El pato nada\n"; }
};

int main() {
    Pato p;
    p.volar();
    p.nadar();
    return 0;
}
