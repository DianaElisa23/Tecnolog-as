public class MaquinaCafe {
    private String tipoCafe;

    public MaquinaCafe(String tipoCafe){
        this.tipoCafe = tipoCafe;
    }

    public void PrepararCafe(){
        System.out.println("Preparando un cafe: " + tipoCafe);
    }
}
