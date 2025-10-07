using System;

namespace buenEjemplo
{
    public interface pagarConNFC
    {
        void Pagar(string numeroTarjeta, double monto);
    }
}