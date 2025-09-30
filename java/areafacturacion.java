package java;
import java.util.Scanner;
public class areafacturacion {
    public static void main(String[] args) {
      System.out.println("digite el valor que desea evaluar para la facturacion");
      Scanner var = new Scanner(System.in);
      int num = 0;
      num = Integer.valueOf(var.nextLine());
      if (num%2==0){
        System.out.println("el numero es par");
      }else{
        System.out.println("el numero no es par");
      }
      var.close();
    }
    
}
