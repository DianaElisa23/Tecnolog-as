using System;

namespace SinLSP;

public class Program
{
    public static void Main()
    {
        Empleado e1 = new EmpleadoTiempoCompleto();
        Emopleado e2 = new Pasante();


        Console.WriteLine("Empleado a tiempo completo: ");
        Console.WriteLine($"Salario: " { e1.CalcularSalario});
        e1.Trabajar();

        console.WriteLine("Pasante: ");
        
    }
}