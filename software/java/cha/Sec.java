import java.util.Scanner;

public class Sec {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Inserire la frase: ");
        String frase = scanner.nextLine();
        frase = frase.toLowerCase();
        frase = frase.replaceAll(" ", "");
        frase = frase.replaceAll("[^a-zA-Z0-9]", "");
        boolean right_one = true;

        char[] array_frase = frase.toCharArray();
        char[] opposite_phrase = new char[array_frase.length];
        int j = 0;
        for (int i = array_frase.length - 1; i > -1; i--) {
            opposite_phrase[j] = array_frase[i];
            j++;
        }
        for (int a = 0; a < opposite_phrase.length; a++) {
            if (opposite_phrase[a] != array_frase[a]) {
                right_one = false;
            }
        }

        if (right_one == false) {
            System.out.println("Non sono palindrome!");
        } else {
            System.out.println("Sono palindrome!");
        }
    }
}