import java.io.*;
import java.util.*;

public class Baekjoon17276 {

  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(bf.readLine());
    for(int i = 0; i < T ; i++){
        String[] array = bf.readLine().split(" ");
        int n = Integer.parseInt(array[0]);
        int d = Integer.parseInt(array[1]);

        int[][] baseArr = new int[n][n];

        for(int j = 0; j < n ; j++){
          String[] line = bf.readLine().split(" ");
          for(int k = 0; k < n; k++){
            baseArr[j][k] = Integer.parseInt(line[k]);
          }
        }

        if(d == 360 || d == -360){
          Baekjoon17276.printArr(baseArr, n);
          
        }else{
          if(d < 0){
            d = 360 + d;
          }

          int rotateCount = d / 45;
          
          for(int j = 0; j < rotateCount; j++ ){
            baseArr = Baekjoon17276.rotate45(baseArr, n);
          }

          Baekjoon17276.printArr(baseArr, n);
        }


    }
  }

  public static void printArr(int[][] arr, int n ){

    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        System.out.print(arr[i][j] + " ");
      }
      System.out.println();
    }
  }

  public static int[][] rotate45(int[][] base, int n){

    int[][] newArr = new int[n][n];
    int middle = ((n+1)/ 2) - 1;

    for(int i = 0; i < n ;i++){
      for(int j = 0; j < n; j++){
        newArr[i][j] = base[i][j];
      }
    }

    //주 대각선
    for(int i = 0; i < n; i++){
      //주 대각선
      newArr[i][middle] = base[i][i];
      //가운데 열
      newArr[i][n - 1 - i] = base[i][middle];
      //부대각선
      newArr[middle][n - 1 - i] = base[i][n - 1 -i];
      //가운데 행
      newArr[i][i]  = base[middle][i]; 
    }
    


    return newArr;

  }

  
  
}
