import java.io.*;
import java.util.*;

public class Baekjoon1244 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer switchNum = Integer.parseInt(br.readLine());
        String[] switches = new String[switchNum];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < switchNum; i++) {
            switches[i] = st.nextToken();
        }
        Integer studentNum = Integer.parseInt(br.readLine());

        for (int i = 0; i < studentNum; i++) {
            String[] student = br.readLine().split(" ");
            Integer gender = Integer.parseInt(student[0]);
            Integer number = Integer.parseInt(student[1]);

            if (gender == 1) {
                // 남학생은 number의 배수 스위치들을 변경
                for (int j = number - 1; j < switchNum; j += number) {
                    switches[j] = switches[j].equals("1") ? "0" : "1";
                }
            } else {
                // 여학생의 경우 대칭을 고려하여 스위치 변경
                int left = number - 1;
                int right = number - 1;

                // 가운데 스위치 변경
                switches[left] = switches[left].equals("1") ? "0" : "1";

                // 좌우 대칭을 고려하여 스위치 변경
                while (left > 0 && right < switchNum - 1) {
                    if (switches[left - 1].equals(switches[right + 1])) {
                        left--;
                        right++;
                        switches[left] = switches[left].equals("1") ? "0" : "1";
                        switches[right] = switches[right].equals("1") ? "0" : "1";
                    } else {
                        break;
                    }
                }
            }
        }

        // 스위치를 20개씩 출력
        for (int i = 0; i < switchNum; i += 20) {
            for (int j = i; j < Math.min(i + 20, switchNum); j++) {
                System.out.print(switches[j] + " ");
            }
            System.out.println(); // 줄 바꿈
        }
    }
}
