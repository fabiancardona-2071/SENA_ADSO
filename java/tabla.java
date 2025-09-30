package java;
import java.util.Scanner;
public class tabla {
    public static void main(String[] args) {
        System.out.println("digite que numero quiere saber su tabla de multiplicar");
        Scanner sc = new Scanner(System.in);
        int num=0;
        int j=1;
        int table;
        num=Integer.valueOf(sc.nextLine());
        for (int i=1;i<=10;i++){
            table= num*i;
            System.out.println(num+"*"+i+"="+table);
        }


    }
    
}
