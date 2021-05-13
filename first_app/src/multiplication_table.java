public class multiplication_table {
    public static void main(String[] args) {
        for(int i = 0;i<10;i++){
            for(int x = 10;x>0;x--){
                int z = i*x;
                System.out.printf("%d * %d = %d", x , i , x * i ).println();
            }
        }
    }

}
