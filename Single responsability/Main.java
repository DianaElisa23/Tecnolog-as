public class Main {
    public static void main(String[] args) {
        SistemaPedidos pedidos = new SistemaPedidos("Diana", "Capuchino");
        MaquinaCafe maquina = new MaquinaCafe("Capuchino");
        Factura factura = new Factura("Diana", 85.50);
        Notificación notificacion = new Notificación("Diana", "Tu café está listo");

        pedidos.tomarPedido();
        maquina.PrepararCafe();
        factura.generarFactura();
        notificacion.enviarCorreo();
    }
}
