'''''import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class simple_calculator_failed {
    static void eval(String scan) {
        /* Create stacks for operators and operands */
        Stack<Integer> op = new Stack<Integer>();
        Stack<Double> val = new Stack<Double>();
        /* Create temporary stacks for operators and operands */
        Stack<Integer> optmp = new Stack<Integer>();
        Stack<Double> valtmp = new Stack<Double>();
        /* Accept expression */
        String input = scan;
        input = "0" + input;
        input = input.replaceAll("-", "+-");
        /* Store operands and operators in respective stacks */
        String temp = "";
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '-')
                temp = "-" + temp;
            else if (ch != '+' && ch != '*' && ch != '/')
                temp = temp + ch;
            else {
                val.push(Double.parseDouble(temp));
                op.push((int) ch);
                temp = "";
            }
        }
        val.push(Double.parseDouble(temp));
        /* Create char array of operators as per precedence */
        /* -ve sign is already taken care of while storing */
        char operators[] = {'/', '*', '+'};
        /* Evaluation of expression */
        for (int i = 0; i < 3; i++) {
            boolean it = false;
            while (!op.isEmpty()) {
                int optr = op.pop();
                double v1 = val.pop();
                double v2 = val.pop();
                if (optr == operators[i]) {
                    /* if operator matches evaluate and store in temporary stack */
                    if (i == 0) {
                        valtmp.push(v2 / v1);
                        it = true;
                        break;
                    } else if (i == 1) {
                        valtmp.push(v2 * v1);
                        it = true;
                        break;
                    } else if (i == 2) {
                        valtmp.push(v2 + v1);
                        it = true;
                        break;
                    }
                } else {
                    valtmp.push(v1);
                    val.push(v2);
                    optmp.push(optr);
                }
            }
            /* Push back all elements from temporary stacks to main stacks */
            while (!valtmp.isEmpty())
                val.push(valtmp.pop());
            while (!optmp.isEmpty())
                op.push(optmp.pop());
            /* Iterate again for same operator */
            if (it)
                i--;
        }
    }
    public static void main(String[] args) throws ScriptException{
        Scanner obj = new Scanner(System.in);
        System.out.println("enter an oper: ");
        String operation = obj.nextLine();
        ArrayList <String> number = new ArrayList<String>();
        for(int i = 0; i <2; i++) {
            Scanner num = new Scanner(System.in);
            System.out.printf("enter the %d number: ", i).println();
            String nums = num.nextLine();
            number.add(nums);
            ScriptEngineManager manager = new ScriptEngineManager();
            ScriptEngine engine = manager.getEngineByName("Java");
            String result = String.join(operation, number);
            int zz = eval(result);
        }
        System.out.println();
    }
}
'''''