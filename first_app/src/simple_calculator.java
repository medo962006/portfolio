import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;
import java.util.ArrayList;
import java.util.Scanner;
public class simple_calculator {
    public static void main(String[] args) throws ScriptException, NullPointerException {
        Scanner obj = new Scanner(System.in);
        System.out.println("enter an oper: ");
        String operation = obj.nextLine();
        ArrayList <String> number = new ArrayList<String>();
        for(int i = 0; i <2; i++){
            Scanner num = new Scanner(System.in);
            System.out.printf("enter the %d number: ",i).println();
            String nums = num.nextLine();
            number.add(nums);
            ScriptEngineManager manager = new ScriptEngineManager();
            ScriptEngine engine = manager.getEngineByName("Java");
            String result = String.join(operation , number);
            System.out.println(engine.eval(result));
        }

        System.out.println();
    }
}
