import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Baekjoon2309 {

  public static void combinations(ArrayList<Integer> index, int n,int[] target, ArrayList<Integer> result, ArrayList<ArrayList<Integer>> output){

    if(result.size() == n){
      output.add(result);
      return;
    }

    for(int i = 0 ; i < target.length ; i++){
      if(index.indexOf(i) == -1){

        ArrayList<Integer> copiedResult = (ArrayList<Integer>) result.clone();
        ArrayList<Integer> copiedIndex = (ArrayList<Integer>) index.clone();
        copiedResult.add(target[i]);
        copiedIndex.add(i);
        combinations(copiedIndex, n, target, copiedResult, output );
      }
    }

  }

  public static void main(String[] args) throws IOException{

    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));



    int[] arr = new int[9];

    for(int i =0  ; i< 9 ; i++){
      arr[i] = Integer.parseInt(bf.readLine());
    }

    ArrayList<ArrayList<Integer> > output = new ArrayList<>();


    combinations(new ArrayList<>(), 7, arr, new ArrayList<>(), output);

    for(ArrayList<Integer> re : output){
      int sum = 0;

      for(Integer i : re){
        sum += i;
      }

      if(sum == 100){
        Collections.sort(re);
        for(Integer i  :re){
          System.out.println(i);
        }
        break;
      }



    }

  }
  
}
