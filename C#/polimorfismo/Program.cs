using System;
using TiposdePolimorfismo.Utilidades;
using TiposdePolimorfismo.Figuras;  
using TiposdePolimorfismo.Genericos;
using TiposdePolimorfismo.Coerción;


class Program
{
    public static void Main(string[] args)
    {
        List<Fiogura> figuras = new List<Figura>();
        {
            new Circulo(5),
            new Rectangulo(4, 6)
        };


        foreach (var f in figuras)
        {
            f.dibujar();
            Console.WriteLine($"Area: {f.calcularArea()}");
        }

        Caja<string> caja1 = new Caja<string>();
        caja1.Guardar("Hola Mundo");
        Console.WriteLine($"Contenido de la caja1: {caja1.Abrir()}");   

        Caja<int> caja2 = new Caja<int>();
        caja2.Guardar(123);
        Console.WriteLine($"Contenido de la caja2: {caja2.Abrir()}");

        Calculadora calc = new Calculadora();
        Console.WriteLine($"Suma de enteros: {calc.Sumar(5, 10)}");
        Console.WriteLine($"Suma de decimales: {calc.Sumar(5.5, 10.3)}");
        
        Metro m = 10.56m;
        double d = 









    }
}