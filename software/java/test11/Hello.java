import java.util.Scanner;
import java.util.ArrayList;

public class Hello {
    public static Number numbersAdd(float num1, float num2) {
        return (num1 + num2);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> test = new ArrayList<>();
        System.out.print("Ciao mondo, inserisci il tuo nome: ");
        String name = scanner.nextLine();
        test.add(name);
        System.out.print("Inserisci il tuo soprannome: ");
        String username = scanner.nextLine();
        test.add(username);

        for (String a : test) {
            System.out.println(a);
        }

        System.out.print("Inserire il primo numero: ");
        float x = scanner.nextFloat();
        scanner.nextLine();
        System.out.print("Inserire il secondo numero: ");
        float y = scanner.nextFloat();
        scanner.nextLine();

        System.out.println(numbersAdd(x,y));
    }
}
