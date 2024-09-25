import java.util.*;
import java.io.*;

public class Baekjoon1753 {

    static class Node implements Comparable<Node> {
        int vertex;
        int weight;

        public Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.weight, other.weight);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(bf.readLine());

        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, w));  // u에서 v로 가는 가중치 w인 간선 추가
        }

        int[] distance = new int[V + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);  // 최댓값으로 초기화

        // 다익스트라 알고리즘 실행
        dijkstra(K, graph, distance);

        // 결과 출력
        for (int i = 1; i <= V; i++) {
            if (distance[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(distance[i]);
            }
        }
    }

    public static void dijkstra(int start, ArrayList<ArrayList<Node>> graph, int[] distance) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        distance[start] = 0;
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentVertex = current.vertex;
            int currentWeight = current.weight;

            if (currentWeight > distance[currentVertex]) {
                continue;  // 이미 처리된 정점이면 무시
            }

            for (Node neighbor : graph.get(currentVertex)) {
                int nextVertex = neighbor.vertex;
                int nextWeight = currentWeight + neighbor.weight;

                if (nextWeight < distance[nextVertex]) {
                    distance[nextVertex] = nextWeight;
                    pq.offer(new Node(nextVertex, nextWeight));
                }
            }
        }
    }
}
