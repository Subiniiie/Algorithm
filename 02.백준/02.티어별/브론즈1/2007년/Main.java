import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        int month, day, resultDay;
        String result;
        List<String> list = new ArrayList<>();
        list.add("MON");
        list.add("TUE");
        list.add("WED");
        list.add("THU");
        list.add("FRI");
        list.add("SAT");
        list.add("SUN");
        Scanner sc = new Scanner(System.in);
        month = sc.nextInt();
        day = sc.nextInt();

        if (month == 1) {
            resultDay = day % 7;
            result = list.get(resultDay);
        } else if (month == 2) {
            
        }

    }
}
