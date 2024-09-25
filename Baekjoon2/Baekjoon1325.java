import java.util.*;
import java.io.*;

public class Baekjoon1325 {

  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    String[] fristLine = bf.readLine().split(" ");
    int N = Integer.parseInt(fristLine[0]);
    int M = Integer.parseInt(fristLine[1]);

    ArrayList<ArrayList<Integer>> nodes = new ArrayList<>();

    for(int i = 0; i < N + 1; i++){
      nodes.add(new ArrayList<>());
    }

    for(int i = 0; i < M ; i++){
      String[] computers = bf.readLine().split(" ");
      int A = Integer.parseInt(computers[0]);
      int B = Integer.parseInt(computers[1]);
      // System.out.println(A + " " + B);
      nodes.get(B).add(A);
    }


    int maxSize = 0;
    ArrayList<Integer> result = new ArrayList<>();

    for(int i = 1; i < N + 1; i++){
      boolean[] visited = new boolean[N + 1];
      ArrayList<Integer> tmpResult = new ArrayList<>();


      dfs(nodes,visited, i, tmpResult);

      if(tmpResult.size() > maxSize){
        result.clear();
        result.add(i);
        maxSize = tmpResult.size();
      }else if(tmpResult.size() == maxSize){
        result.add(i);
      }
    }

    Collections.sort(result);

    for(Integer r : result){
      System.out.print(r + " ");
    }
    
  }

  public static void dfs( ArrayList<ArrayList<Integer>> nodes, boolean[] visited, int start, ArrayList<Integer> result){
      visited[start] = true;


      for(Integer node : nodes.get(start)){
        if(!visited[node]){
          result.add(node);
          dfs(nodes,visited, node, result);
        }
      }


  }
  
}
