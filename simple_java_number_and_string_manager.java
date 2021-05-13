import java.util.Scanner;
public class Solution {

    public static void simple_java_number_and_string_manager(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            String zero = "0";
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                String str = String.valueOf(x);
                StringBuilder myName = new StringBuilder(str);
                if (str.length() == 2){
                    myName.insert(0, '0');
                }else if (str.length() == 1){
                    myName.insert(0, "00");
                }
                
                String spaces = " ".repeat(15-s1.length());
                System.out.println(s1+spaces+myName);
            }
            System.out.println("================================");

    }
}