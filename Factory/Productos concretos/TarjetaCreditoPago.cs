using System; 

namespace ProductosConcretos
{
    public class TarjetaCreditoPago : IPago
    {
        public void ProcesarPago(decimal monto)
        {
            Console.WriteLine($"Procesando pago de ${monto} con Tarjeta de Crédito.");
            
        }

        public bool ValidarPago()
        {
            Console.WriteLine("Validando detalles de la Tarjeta de Crédito (número, fecha, CVV).");
            return true; 
        }
    }
}