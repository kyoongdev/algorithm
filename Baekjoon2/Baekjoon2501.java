import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Baekjoon2501{
  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] fristLine = bf.readLine().split(" ");
    int N = Integer.parseInt(fristLine[0]);
    int K = Integer.parseInt(fristLine[1]);


    int[] arr = new int[N];
    int index = 0;
    for(int i = 1 ; i <= N ; i++){
      if(N % i == 0){
        arr[index] = i;
        index++;
      }
    }


    System.out.println(arr[K - 1]);
    
  }
}