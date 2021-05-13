import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class Helloworld {
    public static void main(String[] args) {
        ArrayList <String> names = new ArrayList<String>();
        List<String> list = Arrays.asList("a","b","c");

        for(int i = 0;i<3;i++){
            Scanner myObj = new Scanner(System.in);
            String userName;

            // Enter username and press Enter
            System.out.println("Enter username");
            userName = myObj.nextLine();
            names.add(userName);
        }
        String result = String.join(",", names);
        System.out.println(result);

    }
    public static void main() {
        // Prints "Hello, World" to the terminal window.
        for(int i = 0 ; i<11; i ++){
            System.out.println("hello, world");
        }
    }
}
