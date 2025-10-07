namespace sinLSP;

public class Pasante : Empleado
{
    public override decimal CalcularSalario()
    {
        throw new NotImplementedException("Los pasantes no tienen un salario fijo");
    }

}