import java.io.*;
import java.util.*;

public class Baekjoon2578 {

  private static int countBingo(String[][] bingo){
    //세로
    int bingoCount = 0;
    for(int i = 0 ; i < 5; i++){
      int count = 0;
      for(int j = 0; j < 5; j++){
        if(bingo[j][i].equals("*")){
          count += 1;
        }
      }

      if(count == 5){
        bingoCount += 1;
      }
    }

    //가로
    for(int i = 0 ; i < 5; i++){
      int count = 0;
      for(int j = 0; j < 5; j++){
        if(bingo[i][j].equals("*")){
          count += 1;
        }
      }

      if(count == 5){
        bingoCount += 1;
      }
    }

    //대각선
    int leftCount = 0;
    int rightCount = 0;
    for(int i = 0; i < 5; i++){
      
      if(bingo[i][i].equals("*")){
        leftCount += 1;
      }

      if(bingo[i][5 - i - 1].equals("*")){
        rightCount += 1;

      }
    }

    if(leftCount == 5){
      bingoCount += 1;
    }
    if(rightCount == 5){
      bingoCount += 1;
    }

    return bingoCount;
  }

  public static void main(String[] args)throws IOException {
    BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

    String[][] bingo = new String[5][5];
    String[][] numbers = new String[5][5];

    for(int i = 0 ; i < 5; i++){
      bingo[i] = br.readLine().split(" ");
    }


    for(int i = 0 ; i < 5 ; i++){
      numbers[i] =  br.readLine().split(" ");
    }   
    int count = 0;
    boolean isBingo= false;
    
    for(int i = 0; i < 5; i++){
      for(int j = 0; j < 5 ; j++){
        String number = numbers[i][j];

          count += 1;
          for (int l = 0 ; l < 5 ; l++){
            for (int k = 0 ; k < 5 ; k++){
              if(bingo[l][k].equals(number)){
                bingo[l][k] = "*";
              }
  
            }
          }
          int bingoCount = Baekjoon2578.countBingo(bingo);
          
          if(bingoCount >= 3){
            isBingo = true;
            break;
          }
      }

      if(isBingo){
        break;
      }
    }

    System.out.println(count);
    
  }


  
}
