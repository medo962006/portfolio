
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class simple_string_purifier{



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        scanner.close();
        if(n%2!=0){
            System.out.println("Weird");
        }else{
            if(n<6 && n>1){
                System.out.println("Not Weird");
            }else if(n<20 && n>5){
                System.out.println("Weird");
            }else if(n>20){
                System.out.println("Not Weird");
            }
        }
    }
}