public class WhatsApp implements Notificador {
    @Override
    public void enviar(String mensaje){
        System.out.println("Enviando WhatsApp " + mensaje);
    }
}
