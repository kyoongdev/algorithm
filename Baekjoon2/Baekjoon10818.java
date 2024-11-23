import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Baekjoon10818 {

  public static void main(String[] args) throws IOException{
    BufferedReader bf =  new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(bf.readLine());

    String[] arr = bf.readLine().split(" ");

    int maxValue = -1000000;
    int minValue = 1000000;

    for(int i = 0; i < arr.length ; i++){
      minValue = Math.min(minValue, Integer.parseInt(arr[i]));
      maxValue = Math.max(maxValue , Integer.parseInt(arr[i]));
    }



    System.out.println(minValue + " " + maxValue);
  }
  
}
