import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        boolean local = false;
        BufferedReader br;
        if (local) {
            br = new BufferedReader(new FileReader("../../../input.txt"));
        } else {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append("\n");
        }
        
        StringTokenizer st = new StringTokenizer(sb.toString());
        
        int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        int T = Integer.parseInt(st.nextToken());
        for (int t = 0; t < T; ++t) {
            int n = Integer.parseInt(st.nextToken());
            int[][] sea = new int[n][n];
            int[][] visited = new int[n][n];

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    visited[i][j] = -1;
                }
            }
            
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    sea[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int sx = Integer.parseInt(st.nextToken()), sy = Integer.parseInt(st.nextToken());
            int ex = Integer.parseInt(st.nextToken()), ey = Integer.parseInt(st.nextToken());

            Deque<int[]> q = new LinkedList<>();
            int time = 0;
            q.add(new int[]{sx, sy, time});
            visited[sx][sy] = 0;

            while (!q.isEmpty()) {
                int[] cur = q.pollFirst();
                int cx = cur[0], cy = cur[1], ct = cur[2];
                for (int i = 0; i < 4; ++i) {
                    int nx = cx + dir[i][0], ny = cy + dir[i][1];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if (sea[nx][ny] == 1) continue;
                    else if (sea[nx][ny] == 2) {
                        int able = ct + (3 - ct % 3);
                        if (visited[nx][ny] == -1 || visited[nx][ny] > able) {
                            if (able - ct > 1) {
                                q.addLast(new int[]{nx, ny, able});
                            } else {
                                q.addFirst(new int[]{nx, ny, able});
                            }
                            visited[nx][ny] = able;
                        }
                    } else {
                        if (visited[nx][ny] == -1 || visited[nx][ny] > ct + 1) {
                            q.addFirst(new int[]{nx, ny, ct + 1});
                            visited[nx][ny] = ct + 1;
                        }
                    }
                }
            }
            bw.write(String.format("#%d %d\n", t + 1, visited[ex][ey]));
        }
        bw.flush();
        bw.close();
    }
}
