import java.util.ArrayList;

class Prima {
    public static void main(String[] args) {
        int[] arraynum = {1,2,-4,5,-7,8,9,0,0};

        int positivi = 0;
        int negativi = 0;
        int neutri = 0;

        for (int a : arraynum) {
            if (a > 0) {
                System.out.println("Il numero " + a + " è positivo");
                positivi++;
            } else if (a == 0) {
                System.out.println("Il numero " + a + " è neutro");
                neutri++;
            } else if (a < 0) {
                System.out.println("Il numero " + a + " è negativo");
                negativi++;
            } else {
                System.out.println(a + " non è un numero!");
            }
        }
        
        System.out.println("Nummeri positivi: " + positivi);
        System.out.println("Nummeri negativi: " + negativi);
        System.out.println("Nummeri neutri: " + neutri);
    }
}