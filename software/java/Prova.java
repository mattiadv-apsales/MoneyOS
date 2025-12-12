import java.util.Scanner;
import java.util.ArrayList;

class people {

    static ArrayList<people> array_people = new ArrayList<>();
    String name;
    String cognome;
    int eta;

    public people(String nome, String cognome, int eta) {
        this.name = nome;
        this.cognome = cognome;
        this.eta = eta;

        array_people.add(this);
    }

    public static void show_all_people() {
        int count = 1;
        for (people a : array_people) {
            Prova.stampa(count + ") " + a.name + " " + a.cognome + " " + a.eta, 0);
            count++;
        }
    }

    public static void research_people(String name) {
        boolean found = false;
        for (people a : array_people) {
            if (a.name.equals(name)) {
                Prova.stampa("Founded: " + a.name + " " + a.cognome + " " + a.eta, 0);
                found = true;
            }
        }

        if (found == false) {
            Prova.stampa("Mi dispiace ma l'utente con nome " + name + " non è stato trovato!", 0);
        }
    }

    public static void research_people_surname(String surname) {
        boolean found = false;
        for (people a : array_people) {
            if (a.cognome.equals(surname)) {
                Prova.stampa("Founded: " + a.name + " " + a.cognome + " " + a.eta, 0);
                found = true;
            }
        }

        if (found == false) {
            Prova.stampa("Mi dispiace ma l'utente con cognome " + surname + " non è stato trovato!", 0);
        }
    }

    public static void research_people_eta(int eta) {
        boolean found = false;
        for (people a : array_people) {
            if (a.eta == eta) {
                Prova.stampa("Founded: " + a.name + " " + a.cognome + " " + a.eta, 0);
                found = true;
            }
        }

        if (found == false) {
            Prova.stampa("Mi dispiace ma l'utente con eta " + eta + " non è stato trovato!", 0);
        }
    }

    public void salud() {
        Prova.stampa("Ciao io sono " + this.name + " " + this.cognome + " e ho " + this.eta + " anni", 0);
    }
}

class Prova {
    public static void stampa(Object frase, int type) {
        if (type == 0) {
            System.out.println(frase);
        } else { 
            System.out.print(frase);
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean start = true;

        while (start) {
            stampa("\n\n1) Aggiungi\n2) Stampa\n3) Cerca per nome\n4) Cerca per cognome\n5) Cerca per eta\n6) Esci\nScegli: ", 1);
            String scelta = scanner.nextLine();

            if (scelta.equals("1")) {
                stampa("\n\nInserire nome: ", 1);
                String nome = scanner.nextLine();
                stampa("Inserire cognome: ", 1);
                String cognome = scanner.nextLine();
                stampa("Inserire eta: ", 1);
                int eta = scanner.nextInt();
                scanner.nextLine();

                people new_people = new people(nome, cognome, eta);
            } else if (scelta.equals("2")) {
                people.show_all_people();
            } else if(scelta.equals("3")) {
                stampa("\n\nInserire nome da ricercare: ", 1);
                String name = scanner.nextLine();
                people.research_people(name);
            } else if (scelta.equals("4")) {
                stampa("\n\nInserire cognome da ricercare: ", 1);
                String cognome = scanner.nextLine();
                people.research_people_surname(cognome);
            } else if(scelta.equals("5")) {
                stampa("\n\nInserire eta da ricercare: ", 1);
                int eta = scanner.nextInt();
                scanner.nextLine();
                people.research_people_eta(eta);
            } else if (scelta.equals("6")) {
                start = false;
            } else {
                stampa("\n\nInserire un valore valido!\n\n", 0);
            }
        }
    }
}