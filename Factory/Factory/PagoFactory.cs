using Productos;
using ProductosConcretos;

namespace Factory
{
    public static class PagoFactory
    {
        public static IPago crearPago(TipoPago tipoPago)
        {
            return tipoPago switch
            {
                TipoPago.TarjetaCredito => new TarjetaCreditoPago(),
                TipoPago.PayPal => new PayPalPago(),
                TipoPago.Transferencia => new TransferenciaPago(),
            }; 
    }
}