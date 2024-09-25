import java.util.*;
import java.io.*;

public class Baekjoon20291 {
  public static void main(String[] args) throws IOException{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(bf.readLine());
    Map<String,Integer> files = new HashMap<>();
    

    for(int i = 0; i < N; i++){
      String[] info = bf.readLine().split("\\.");
      String file = info[1];

      
      if(files.containsKey(file)){
        Integer count =  files.get(file);
        files.put(file, count + 1);
      }else{
        files.put(file, 1);
      }

    }
     Set<String> fileNames =    files.keySet();

     ArrayList<String> fileNameForSort = new ArrayList<>(fileNames);

     Collections.sort(fileNameForSort);

     for(String f : fileNameForSort){
        System.out.println(f + " " +files.get(f));
     }
  }
}
