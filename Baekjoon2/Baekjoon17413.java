import java.io.*;
import java.util.*;

public class Baekjoon17413 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String input = bf.readLine();
        StringBuilder result = new StringBuilder(); 
        Stack<Character> stack = new Stack<>(); 
        boolean inTag = false; 

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (c == '<') {
                
                while (!stack.isEmpty()) {
                    result.append(stack.pop());
                }
                inTag = true;
                result.append(c); 
            } else if (c == '>') {
                inTag = false;
                result.append(c); 
            } else if (inTag) {
                result.append(c); 
            } else {

                if (c == ' ') {
                    while (!stack.isEmpty()) {
                        result.append(stack.pop());
                    }
                    result.append(c);
                } else {
                    stack.push(c);
                }
            }
        }


        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }

        System.out.println(result.toString()); // 최종 결과 출력
    }
}
