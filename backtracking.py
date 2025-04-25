N = 5  # 미로의 크기 (5x5)

# 미로 (1은 벽, 0은 통로)
maze = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]
]

# 출발점과 목표점
solution = [[0 for _ in range(N)] for _ in range(N)]

# 이동할 방향 (위, 아래, 왼쪽, 오른쪽)
row_moves = [-1, 1, 0, 0]
col_moves = [0, 0, -1, 1]

def is_safe(row, col):
    return 0 <= row < N and 0 <= col < N and maze[row][col] == 0 and solution[row][col] == 0

def solve_maze(row, col):
    # 목표지점에 도달한 경우
    if row == N - 1 and col == N - 1:
        solution[row][col] = 1
        return True
    
    if is_safe(row, col):
        # 현재 경로를 방문했다고 표시
        solution[row][col] = 1

        # 네 방향으로 탐색 (위, 아래, 왼쪽, 오른쪽)
        for i in range(4):
            new_row = row + row_moves[i]
            new_col = col + col_moves[i]

            if solve_maze(new_row, new_col):
                return True

            # 백트래킹: 경로가 막히면 돌아가기
            solution[row][col] = 0

    return False

def print_solution():
    for row in solution:
        print(" ".join(str(cell) for cell in row))

# 미로를 해결하기
if solve_maze(0, 0):
    print_solution()
else:
    print("경로를 찾을 수 없습니다..")
