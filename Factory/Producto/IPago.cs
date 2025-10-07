namespace Producto
{
    public interface IPago
    {
        void ProcesarPago(decimal momnto);
        void validar();
    }
}