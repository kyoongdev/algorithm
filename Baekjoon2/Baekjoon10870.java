import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Baekjoon10870 {


  public static int fibo(int n){
    int[] dp = new int[n + 2];
    dp[0] = 0;
    dp[1] = 1;

    for (int i  = 2 ; i <= n ; i++){
      dp[i] = dp[i-1] + dp[i-2];
    }


    return dp[n];
  }

  public static void main(String[] args) throws IOException{

    BufferedReader bf =  new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(bf.readLine());

    System.out.println(fibo(N));
    
  }
  
}
