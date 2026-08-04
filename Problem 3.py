class Printer {
    private static Printer instance;

    private Printer() {
        System.out.println("Printer Created");
    }

    public static Printer getInstance() {
        if (instance == null) {
            instance = new Printer();
        }
        return instance;
    }

    public void print(String document) {
        System.out.println("Printing: " + document);
    }
}

public class SingletonDemo {
    public static void main(String[] args) {
        Printer user1 = Printer.getInstance();
        Printer user2 = Printer.getInstance();

        user1.print("Assignment.pdf");
        user2.print("Report.docx");

        if (user1 == user2) {
            System.out.println("Only one Printer object exists.");
        } else {
            System.out.println("Different Printer objects exist.");
        }
    }
}
