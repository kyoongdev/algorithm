import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon2460 {

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int maxPeople = 0;
    int currentPeople = 0;
    for(int i  = 0 ; i < 10 ; i++){
      String[] line = bf.readLine().split(" ");

      int minus = Integer.parseInt(line[0]);
      int plus = Integer.parseInt(line[1]);

      currentPeople += plus;
      currentPeople -= minus;

      maxPeople = Math.max(maxPeople, currentPeople);

    }

    System.out.println(maxPeople);
    
  }
  
}
