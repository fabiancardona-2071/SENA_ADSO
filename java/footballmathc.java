package java;
import java.util.Scanner;

public class footballmathc {
    public static void main(String[] args) {
        int ganador =0;
        int perdedor =0;
        int empate =0;
        int puntos=0;
        System.out.println("digite la cantidad de partidos ganados ");
        Scanner variable = new Scanner(System.in);
        ganador = Integer.valueOf(variable.nextLine());
        System.out.println("digite la cantidad de partidos perdidos");
        perdedor= Integer.valueOf(variable.nextLine());
        System.out.println("digite la cantidad de partidos empatados");
        empate= Integer.valueOf(variable.nextLine());

        puntos=((ganador*3)+(perdedor*0)+empate);
        System.out.println("el total de los puntos es: "+puntos);
        variable.close();

    }
    
}
