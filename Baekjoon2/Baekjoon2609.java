import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon2609 {

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] line = bf.readLine().split(" ");

    int N = Integer.parseInt(line[0]);
    int M = Integer.parseInt(line[1]);

    int max = Math.max(N, M);

    int divValue = 1;

    for(int i = 1; i <= max ; i++){
      if(N % i == 0 && M % i == 0){
        divValue = i;
      }
    }

    System.out.println(divValue);
    System.out.println(divValue * N / divValue * M / divValue);
  }
  
}
