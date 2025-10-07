public class ServicioNoti {
    private Correo correo = new correo();
    public void enviar(String mensaje){
        correo.enviar(mensaje);
    }
}
