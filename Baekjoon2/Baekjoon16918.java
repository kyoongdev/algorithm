import java.util.*;
import java.io.*;

public class Baekjoon16918 {
  
  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] firstLine = bf.readLine().split(" ");

    int R = Integer.parseInt(firstLine[0]);
    int C = Integer.parseInt(firstLine[1]);
    int N = Integer.parseInt(firstLine[2]);

    String[][] map = new String[R][C];
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    for(int i = 0 ; i < R ; i++){
      map[i] =  bf.readLine().split("");
    }

    String[][] resultMap = new String[R][C];

    for(int i = 0 ; i < R ; i++){
      for(int j = 0; j < C ; j++ ){
        resultMap[i][j] = "O";
      }
    }

    if(N == 1){
      printArr(map);
      return;
    }else if(N % 2 == 0){
      
      printArr(resultMap);
      return;
    }

    for(int n = 0; n <= (N - 3) / 2 ; n++){

      for(int i = 0 ; i < R ; i++){
        for(int j = 0; j < C ; j++ ){
          if(map[i][j].equals("O")){

            resultMap[i][j] = ".";
            for(int k = 0; k < 4; k++){
              int nx = i + dx[k];
              int ny = j + dy[k];

              if(0 <= nx && nx < R && 0 <= ny && ny < C  ){
                resultMap[nx][ny] = ".";
              }
            }

          }
        }
      }
      for(int i = 0 ; i < R ; i++){
        for(int j = 0; j < C ; j++ ){
          map[i][j] = resultMap[i][j];
          resultMap[i][j] = "O";
        }
      }
    }

    printArr(map);

    
  }

  public static void printArr(String[][] arr){
    for(int i = 0; i < arr.length ; i++){
      for(int j = 0; j < arr[0].length ; j++){
        System.out.print(arr[i][j]);
      }
      System.out.println();
    }
  }
}
