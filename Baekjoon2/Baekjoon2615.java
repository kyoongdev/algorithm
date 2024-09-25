import java.util.*;
import java.io.*;


public class Baekjoon2615 {
  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int[][] board = new int[19][19];

    for(int i = 0; i < 19 ; i++){
      String[] line = bf.readLine().split(" ");

      for(int j = 0; j < 19; j++){
        board[i][j] = Integer.parseInt(line[j]);
      }
    }

    int[] dx = new int[] {1,1,0,-1};
    int[] dy = new int[] {0,1,1,1};
    int stone = -1;
    int x = -1;
    int y = -1;
    
    outerloop:
    for(int i = 0; i < 19; i++){

      for(int j = 0; j < 19; j++){
        if(board[i][j] == 1 || board[i][j] == 2){
          int focus = board[i][j];
          for(int k = 0; k < 4; k++){
            int count = 1;
            int nx = i + dx[k];
            int ny = j + dy[k];

            if(nx < 0 || ny < 0 || nx >= 19 || ny >= 19){
              continue;
            }
            
            
            while(0 <= nx && nx < 19 && 0 <= ny && ny < 19 && board[nx][ny] == focus){
              count++;
              
              if(count == 5){
                
                if(0 <= nx + dx[k]  && nx + dx[k] < 19 
                && 0 <= ny + dy[k] && ny + dy[k] < 19 
                && board[nx + dx[k]][ny + dy[k]] == focus){
                  
                  break;
                 }
    
                 if(0 <= i - dx[k] && i - dx[k] < 19 
                 && 0 <= j - dy[k] && j - dy[k] < 19 
                 && board[i - dx[k]][j - dy[k]] == focus){
                  
                  break;
                 }
                x = i;
                y = j;
                stone = focus;
                break;
              }

              nx += dx[k];
              ny += dy[k];
             
            }
            if(x != -1 && y != -1){
              break;
            }
            
            
          }   
        }

        
      }
      
    }


    if(x == -1 && y == -1){
      System.out.println(0);
    }else{
      System.out.println(stone);
      System.out.println((x + 1) + " " + (y + 1));
    }
    
  }


  
}
