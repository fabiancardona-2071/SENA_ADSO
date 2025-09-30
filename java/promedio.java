package java;
import java.util.Scanner;
public class promedio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nota1=0;
        int nota2=0;
        int nota3=0;
        int eva=0;
        float prom=0;
        System.out.println("digite nota 1: ");
        nota1=Integer.valueOf(sc.nextLine());
        System.out.println("digite la nota 2");
        nota2=Integer.valueOf(sc.nextLine());
        System.out.println("digite la nota 3");
        nota3=Integer.valueOf(sc.nextLine());
        System.out.println("digite la nota de la evaluacion final");
        eva=Integer.valueOf(sc.nextLine());
        prom=(((((nota1+nota2+nota3)/3)*70)/100)+((eva*30)/100));
        System.out.println("el promedio es: "+prom);
        sc.close();

    }
}
