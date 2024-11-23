import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon3460 {

  public static String digit(int n){

    String binary = "";

    while(n != 0){
      int value = n % 2;

      if(value == 0){
        binary = "0" + binary;
      }else{
        binary = "1" + binary;
      }

      n = n / 2;
    }


    return binary;
  }

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(bf.readLine());
    for(int i = 0 ; i < T; i++){
      int N = Integer.parseInt(bf.readLine());
      String binary = digit(N);



      for(int j = 0 ; j < binary.length(); j++){

        if(String.valueOf(binary.charAt(binary.length() - j - 1)).equals("1")){
          System.out.print(j + " ");
        }

      }
      System.out.println();

    }

    
  }
  
}
