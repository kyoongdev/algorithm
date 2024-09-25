import java.io.*;
/**
 * 
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9  2  3  14 33
46 23 8  1  4  15 34
45 22 7  6  5  16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
 */

public class Baekjoon1913 {

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(bf.readLine());
    int target = Integer.parseInt(bf.readLine());

    int[][] board = new int[N][N];
    int start =(int) Math.ceil(N / 2) ;
    board[start][start] = 1;

    int value = 2;

    for(int i = start ; i > 0; i--){
      int x = i;
      int y = i;
      int search = 2 * (start - i + 1);
      // System.out.println("Search : " + search );

      x--;
      for(int j = 0; j < search; j++){  

        if(j != 0){
          y++;
        }

        // System.out.println("1 X , Y : " + x + " " + y+ " " + value );
        board[x][y] = value;
        value++;
      }


      for(int j = 0; j < search; j++){
          x ++;
        
        // System.out.println("2 X , Y : " + x + " " + y + " " + value);
        board[x][y] = value;
        value++;
      }


      for(int j = 0; j < search; j++){
        y--;
        
        // System.out.println("3 X , Y : " + x + " " + y + " " + value);
        board[x][y] = value;
        value++;
      }


      for(int j = 0; j < search; j++){
        x--;
        // System.out.println("4 X , Y : " + x + " " + y + " " + value);
        board[x][y] = value;
        value++;
      }
    }

    int x = 0;
    int y = 0;
    for(int i = 0 ; i < N ; i++){
      for(int j = 0; j < N; j++){
        if(board[i][j] == target){
          x = i + 1;
          y = j + 1;
        }
        System.out.print(board[i][j] + " ");
      }
      System.out.println();
    
    }

    System.out.println(x + " " + y);
  }

  
  
}
