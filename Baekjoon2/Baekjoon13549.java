import java.util.*;
import java.io.*;

public class Baekjoon13549 {
  static int N;
  static int K;
  static int answer = Integer.MAX_VALUE;
  static int[] check;


  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] line = bf.readLine().split(" ");
    N = Integer.parseInt(line[0]);
    K = Integer.parseInt(line[1]);
    check = new int[100001];
    if(N == K){
      System.out.println(0);
      return;
    }
    search();

    System.out.println(answer);

  }

  public static void search(){
    Queue<Integer> que = new LinkedList<>();
    que.offer(N);
    check[N] = 0;
    
    while (!que.isEmpty()) {

        int loc = que.poll();
        int time = check[loc];

        for (int i = 0; i < 3; i++) {
            int newLoc;
            int newTime;

            if(i == 0) {
                newLoc = loc*2;
                newTime = time;
            } else if (i == 1) {
                newLoc = loc + 1;
                newTime = time + 1;
            } else {
                newLoc = loc -1;
                newTime = time + 1;
            }
            

            if(newLoc == K) {
                answer = Math.min(answer, newTime);
                continue;
            }

            if (newLoc >= 0 && newLoc < 100001) {
              
                if(check[newLoc] == 0 || check[newLoc] > newTime){
                    check[newLoc] = newTime;
                    que.add(newLoc);
                }
            }
        }

        if(answer == 1){
          break;
        }
    }
  }

 
  
}
