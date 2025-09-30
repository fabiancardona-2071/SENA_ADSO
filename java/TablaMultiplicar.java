package java;
import java.util.Scanner;

public class TablaMultiplicar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Pedir número al usuario
        System.out.print("Ingrese un número entero: ");
        int numero = sc.nextInt();

        // 2. Generar tabla de multiplicar
        System.out.println("Tabla de multiplicar del " + numero + ":");
        for (int i = 1; i <= 10; i++) {
            int resultado = numero * i;
            System.out.println(numero + " x " + i + " = " + resultado);
        }

        sc.close();
    }
}