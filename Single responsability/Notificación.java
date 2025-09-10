public class Notificación {
    private String cliente;
    private String mensaje;

    public Notificación(String cliente, String mensaje){
        this.cliente = cliente;
        this.mensaje = mensaje;
    }

    public void enviarCorreo(){
        System.out.println(cliente  + ", " +  mensaje);
    }

}
