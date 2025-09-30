package java;
import java.util.Scanner;
public class area_facturacion{
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        System.out.println("Ingrese un Numero Entero: ");
        int num=0;
        num= Integer.valueOf(sc.nextLine());
        if(num%2==0){
            System.out.println("El numero"+num+"Es PAR");
        }else{
            System.out.println("El numero"+num+"es IMPAR");
        }
        sc.close();
    }
}