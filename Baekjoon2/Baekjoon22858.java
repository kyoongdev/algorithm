import java.io.*;
import java.util.*;

public class Baekjoon22858 {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    // 첫 번째 줄 입력 받기 (5 2)
    String[] firstLine = bf.readLine().split(" "); // 공백으로 분리
    
    int n = Integer.parseInt(firstLine[0]); // 5
    int k = Integer.parseInt(firstLine[1]); // 2

    // 두 번째 줄 입력 받기 (4 1 3 5 2)
    String[] secondLine = bf.readLine().split(" ");
    int[] D = new int[n]; // 크기 n인 배열 생성

    for (int i = 0; i < n; i++) {
        D[i] = Integer.parseInt(secondLine[i]);
    }

    // 세 번째 줄 입력 받기 (4 3 1 2 5)
    String[] thirdLine = bf.readLine().split(" ");
    // System.out.println(Arrays.toString(D));
    
    int[] K = new int[n]; // 크기 n인 배열 생성

    for (int i = 0; i < n; i++) {
        K[i] = Integer.parseInt(thirdLine[i]);
    }

    // System.out.println(Arrays.toString(K));

    for(int j = 0 ; j < k ; j++){
      int[] newK = new int[n];
      for(int i = 0 ; i < n ; i++){

        newK[i] = K[D[i] - 1];
        // System.out.println(newK[D[i] - 1] + " " +  D[i] + " " + K[i]);  
      }
      // System.out.println(Arrays.toString(newK));
      K = newK;
    }

    for(int i = 0; i < n ; i++){
      System.out.print(K[i] + " ");

    }


  }
  
}
