import java.io.*;
import java.util.*;

public class Baekjoon15787 {

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = bf.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        // 기차를 이진수로 표현할 정수 배열
        int[] trains = new int[N];
        
        // 명령어 처리
        for (int i = 0; i < M; i++) {
            String[] orders = bf.readLine().split(" ");
            int train = Integer.parseInt(orders[1]) - 1;

            if (orders[0].equals("1")) {
                // 1번 명령어: 좌석에 사람을 태움
                int seat = Integer.parseInt(orders[2]) - 1;
                trains[train] |= (1 << seat);  // 비트 마스크로 해당 좌석을 1로 설정

            } else if (orders[0].equals("2")) {
                // 2번 명령어: 좌석에서 사람을 내림
                int seat = Integer.parseInt(orders[2]) - 1;
                trains[train] &= ~(1 << seat);  // 해당 좌석을 0으로 설정

            } else if (orders[0].equals("3")) {
                // 3번 명령어: 모든 승객을 한 칸씩 뒤로 이동 (좌석 오른쪽으로 시프트)
                trains[train] <<= 1;
                trains[train] &= (1 << 20) - 1;  // 20번째 비트를 0으로 유지

            } else if (orders[0].equals("4")) {
                // 4번 명령어: 모든 승객을 한 칸씩 앞으로 이동 (좌석 왼쪽으로 시프트)
                trains[train] >>= 1;
            }

            System.out.println("TRAINS : " + Arrays.toString(trains));
        }

        // Set을 사용해 중복 제거
        Set<Integer> uniqueTrains = new HashSet<>();
        for (int i = 0; i < N; i++) {
            uniqueTrains.add(trains[i]);
        }

        // 고유한 기차의 수 출력
        System.out.println(uniqueTrains.size());
    }
}
