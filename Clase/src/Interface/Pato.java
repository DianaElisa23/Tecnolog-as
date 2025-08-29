package inter;

public class Pato extends Animal implements Voldador{
    private String color;

    public Pato(int age, String nombre){
        super(age);
        this.color = color;;
    }

    @Override
    public void makeSound(){
        System.out.println("Cuac Cuac");
    }

    @Override
    public void volar(){
        System.out.println("El pato " " está volando con sus " + alas + " alas.");
    }

    public static void main(String[] args){
        Pato pato = new Pato(2, "Paco");
        pato.makeSound();
        pato.volar();
    }
}