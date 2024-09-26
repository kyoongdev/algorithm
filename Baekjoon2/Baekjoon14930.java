import java.io.*;
import java.util.*;

public class Baekjoon14930 {
  public static int[] dx = {1,0,-1,0};
  public static int[] dy = {0,1,0,-1};
  public static int N;
  public static int M;

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] fisrtLine = bf.readLine().split(" ");

     N = Integer.parseInt(fisrtLine[0]);
     M = Integer.parseInt(fisrtLine[1]);
    int[][] map = new int[N][M];
    int[][] resultMap = new int[N][M];

    int startX = -1;
    int startY = -1;
    
    for(int i = 0 ; i < N ; i++){
      String[] mapLine = bf.readLine().split(" ");

      for(int j = 0 ; j < M ; j++){
        map[i][j] = Integer.parseInt(mapLine[j]);
        

        if(map[i][j] == 2){
          startX = i;
          startY = j;
        }


      }
    }

    
    boolean[][] visited = new boolean[N][M];
    visited[startX][startY] = true;


    Queue<Integer[]> queue = new LinkedList<>();

    queue.offer(new Integer[]{startX,startY});

    while(!queue.isEmpty()){
      Integer[] current = queue.poll();

      Integer cx = current[0];
      Integer cy = current[1];

      for(int i = 0 ; i < 4; i++){
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if(0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny] && map[nx][ny] != 0){
          resultMap[nx][ny] = resultMap[cx][cy] + 1;
          visited[nx][ny] = true;
          queue.offer(new Integer[]{nx, ny});
        }
      }

    }

    for(int i = 0 ; i < N ; i++){
      for(int j = 0 ; j < M ; j++){
        if(resultMap[i][j] == 0 && map[i][j] == 1){
          System.out.print(-1 + " ");
        }else{

          System.out.print(resultMap[i][j] + " ");
        }
      }
      System.out.println();
    }

  }


  
}
