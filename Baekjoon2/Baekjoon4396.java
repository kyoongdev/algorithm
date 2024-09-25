import java.io.*;
import java.util.*;

public class Baekjoon4396 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    Integer N = Integer.parseInt(br.readLine());
    String[][] mines = new String[N][N];
    String[][] result = new String[N][N];
    Boolean isMineBoom = false;

    int[] dx = {1,-1,0,0,-1,1,-1,1};
    int[] dy = {0,0,1,-1,1, 1,-1,-1};

    for (int i = 0; i < N ; i++){
      for (int j= 0; j < N ; j++){
        result[i][j]=  ".";
      }
    }



    for(int i = 0 ; i < N; i++){
      mines[i] = br.readLine().split("");
    }

    for(int i = 0 ; i < N; i++){
      String[] clicks = br.readLine().split("");


      for(int j = 0; j < N; j++){
        String click = clicks[j];
        String mine = mines[i][j];

        if(click.equals(".")){
          continue;
        }

        if(mine.equals("*")){
          isMineBoom = true;
          // System.out.println(i + " " + j);

        } 

        int mineCount = 0;
        for(int k = 0; k < 8 ; k++){
          int nx = dx[k] + i;
          int ny = dy[k] + j;

          if(0<= nx && nx < N && 0 <= ny && ny < N && mines[nx][ny].equals("*")){
            mineCount += 1;
          }
        }

        result[i][j] = String.valueOf(mineCount);
      }
   
    }


    if(isMineBoom){
      for (int i = 0; i < N ; i++){
        for (int j= 0; j < N ; j++){
          if(mines[i][j].equals("*")){
            result[i][j]=  "*";
          }
        }
      }
    }

    for(int i = 0 ; i < N; i++){
      for(int j = 0 ; j < N; j++){
        System.out.print(result[i][j]);
      }
      System.out.println();
    }
  }
  
}
