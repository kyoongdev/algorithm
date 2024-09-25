import java.util.*;
import java.io.*;

public class Baekjoon12933 {

  public static void main(String[] args) throws IOException{

    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    String sound = bf.readLine();
    
    int[] stages = new int[5]; // "q", "u", "a", "c", "k"에 해당하는 단계 관리
    int count = 0;
    
    for (char ch : sound.toCharArray()) {
      switch (ch) {
        case 'q':
          if (stages[4] > 0) {
            stages[4]--; // 이전에 완성된 quack에서 q로 돌아간 경우
          } else {
            count++; // 새로운 quack 시작
          }
          stages[0]++;
          break;
          
        case 'u':
          if (stages[0] > 0) {
            stages[0]--;
            stages[1]++;
          } else {
            count = -1; // 순서가 맞지 않음
          }
          break;
          
        case 'a':
          if (stages[1] > 0) {
            stages[1]--;
            stages[2]++;
          } else {
            count = -1;
          }
          break;
          
        case 'c':
          if (stages[2] > 0) {
            stages[2]--;
            stages[3]++;
          } else {
            count = -1;
          }
          break;
          
        case 'k':
          if (stages[3] > 0) {
            stages[3]--;
            stages[4]++;
          } else {
            count = -1;
          }
          break;
          
        default:
          count = -1; // 잘못된 입력
      }
      
      if (count == -1) {
        break; // 에러 발생 시 즉시 종료
      }
    }
    
    // 모든 "quack"이 완성되지 않았으면 에러
    if (count != -1 && (stages[0] != 0 || stages[1] != 0 || stages[2] != 0 || stages[3] != 0)) {
      count = -1;
    }
    
    System.out.println(count);
  }
}
