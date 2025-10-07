using System;


namespace malEjemplo
{
    public string marca;
    public int modelo;
    public int precio;
    public interface RAM;

    public Telefono(string marca, int modelo, int precio, int RAM)
    {
        this.marca = marca;
        this.modelo = modelo;
        this.precio = precio;
        this.RAM = RAM;
    }

    public abstract void escribir();
    public abstract void llamar();
    public abstract void pagarConNFC();
    public abstract void UsarAsistenteVirtual();
    public abstract void desbloquearConHuella();
    

}