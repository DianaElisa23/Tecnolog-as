using System; 

namespace ProductosConcretos 
{
    public class PayPalPago : IPago
    {
        public void ProcesarPago(decimal monto)
        {
            Console.WriteLine($"Procesando pago con Paypal: {monto}"); 
        }

        public bool ValidarPago()
        {
            Console.WriteLine("Validando cuenta con paypal");
            return true;
        }
    }
}