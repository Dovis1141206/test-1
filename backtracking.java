public class MazeSolver {

    static final int N = 5; // 미로의 크기 (5x5)
    
    // 미로 (1은 벽, 0은 통로)
    static int[][] maze = {
        { 1, 0, 0, 0, 0 },
        { 1, 1, 0, 1, 0 },
        { 0, 1, 0, 0, 0 },
        { 0, 1, 1, 1, 0 },
        { 0, 0, 0, 1, 1 }
    };
    
    // 출발점과 목표점
    static int[][] solution = new int[N][N];

    // 이동할 방향 (위, 아래, 왼쪽, 오른쪽)
    static int[] rowMoves = { -1, 1, 0, 0 };
    static int[] colMoves = { 0, 0, -1, 1 };

    public static void main(String[] args) {
        if (solveMaze(0, 0)) {
            printSolution();
        } else {
            System.out.println("경로를 찾을 수 없습니다.");
        }
    }

    // 미로를 해결하는 함수 (백트래킹)
    public static boolean solveMaze(int row, int col) {
        // 목표지점에 도달한 경우
        if (row == N - 1 && col == N - 1) {
            solution[row][col] = 1;
            return true;
        }

        // 현재 위치가 유효하고, 통로인 경우
        if (isSafe(row, col)) {
            // 현재 경로를 방문했다고 표시
            solution[row][col] = 1;

            // 네 방향으로 탐색 (위, 아래, 왼쪽, 오른쪽)
            for (int i = 0; i < 4; i++) {
                int newRow = row + rowMoves[i];
                int newCol = col + colMoves[i];

                if (solveMaze(newRow, newCol)) {
                    return true;
                }

                // 백트래킹: 경로가 막히면 돌아가기
                solution[row][col] = 0;
            }
        }

        return false; // 경로를 찾지 못했을 경우
    }

    // 주어진 위치가 미로 내에서 유효하고, 통로인지를 확인하는 함수
    public static boolean isSafe(int row, int col) {
        return (row >= 0 && row < N && col >= 0 && col < N && maze[row][col] == 0 && solution[row][col] == 0);
    }

    // 해결된 경로 출력 함수
    public static void printSolution() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(solution[i][j] + " ");
            }
            System.out.println();
        }
    }
}
