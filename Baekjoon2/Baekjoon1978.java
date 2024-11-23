import java.io.*;
import java.util.*;

public class Baekjoon1978 {

  public static boolean isPrime(int n ){
    if(n == 1){
      return false;
    }

    if(n == 2){
      return true;
    }

    for(int i = 2; i < (int)Math.sqrt(n) + 1; i++){
      if(n % i == 0){
        return false;
      }
    }

    return true;
  }

  public static void main(String[] args) throws IOException{

    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    String line1 = bf.readLine();

    String[] line2 = bf.readLine().split(" ");


    int count = 0;

    for(String l : line2){

      if(isPrime(Integer.parseInt(l))){
        count++;
      }
    }

    System.out.println(count);
  }
  
}
