「リバーシの操作（斜め）


#python
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    h = int(input_data[0])
    w = int(input_data[1])
    target_y = int(input_data[2])
    target_x = int(input_data[3])
    
    grid = [list(row) for row in input_data[4:]]
    
    grid[target_y][target_x] = '*'
    
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]
    
    for i in range(4):
        path = []
        ny = target_y + dy[i]
        nx = target_x + dx[i]
        
        while 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == '.':
                path.append((ny, nx))
            elif grid[ny][nx] == '*':
                for y, x in path:
                    grid[y][x] = '*'
                break
            
            ny += dy[i]
            nx += dx[i]
            
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    main()



#ans from paiza
H, W, Y, X = map(int, input().split())
s = [list(input()) for _ in range(H)]


def check(x, y, s):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == "*":
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = "*"
                    break


s[Y][X] = "*"
check(X, Y, s)

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()

#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int targetY = sc.nextInt();
        int targetX = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        grid[targetY][targetX] = '*';
        
        int[] dy = {-1, -1, 1, 1};
        int[] dx = {-1, 1, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            List<int[]> path = new ArrayList<>();
            int ny = targetY + dy[i];
            int nx = targetX + dx[i];
            
            while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                if (grid[ny][nx] == '.') {
                    path.add(new int[]{ny, nx});
                } else if (grid[ny][nx] == '*') {
                    for (int[] pos : path) {
                        grid[pos[0]][pos[1]] = '*';
                    }
                    break;
                } else {
                    break;
                }
                ny += dy[i];
                nx += dx[i];
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        sc.close();
    }
}




「リバーシの操作 Java編」

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int targetY = sc.nextInt();
        int targetX = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        grid[targetY][targetX] = '*';
        
        int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        for (int i = 0; i < 8; i++) {
            List<int[]> path = new ArrayList<>();
            int ny = targetY + dy[i];
            int nx = targetX + dx[i];
            
            while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                if (grid[ny][nx] == '.') {
                    path.add(new int[]{ny, nx});
                } else if (grid[ny][nx] == '*') {
                    for (int[] pos : path) {
                        grid[pos[0]][pos[1]] = '*';
                    }
                    break;
                } else {
                    break;
                }
                ny += dy[i];
                nx += dx[i];
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        sc.close();
    }
}


#python

import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

h, w, target_y, target_x = map(int, input_data[:4])
grid = [list(row) for row in input_data[4:]]

grid[target_y][target_x] = '*'

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(8):
    path = []
    ny, nx = target_y + dy[i], target_x + dx[i]
    
    while 0 <= ny < h and 0 <= nx < w:
        if grid[ny][nx] == '.':
            path.append((ny, nx))
        elif grid[ny][nx] == '*':
            for y, x in path:
                grid[y][x] = '*'
            break
        else:
            break
        ny += dy[i]
        nx += dx[i]

for row in grid:
    print("".join(row))



#ans from paiza
H, W, Y, X = map(int, input().split())
s = [list(input()) for _ in range(H)]


def check_diagonal(x, y, s):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == "*":
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = "*"
                    break


def check_row(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W:
                break
            if s[y][x + i * lr] == "*":
                for j in range(1 + i):
                    s[y][x + j * lr] = "*"
                break


def check_column(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H:
                break
            if s[y + i * lr][x] == "*":
                for j in range(1 + i):
                    s[y + j * lr][x] = "*"
                break


s[Y][X] = "*"
check_row(X, Y, s)
check_column(X, Y, s)
check_diagonal(X, Y, s)

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()




いびつなひとりリバーシ（１ターン）
import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

h, w = int(input_data[0]), int(input_data[1])
grid = [list(row) for row in input_data[2:]]

target_y, target_x = -1, -1
for r in range(h):
    for c in range(w):
        if grid[r][c] == '!':
            target_y, target_x = r, c
            grid[r][c] = '*' 
            break

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(8):
    path = []
    ny, nx = target_y + dy[i], target_x + dx[i]
    
    while 0 <= ny < h and 0 <= nx < w:
        if grid[ny][nx] == '.':
            path.append((ny, nx))
        elif grid[ny][nx] == '*':
            for y, x in path:
                grid[y][x] = '*'
            break
        elif grid[ny][nx] == '#':
            break
        ny += dy[i]
        nx += dx[i]

for row in grid:
    print("".join(row))



#ans from paiza
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]


def check_diagonal(x, y, s):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                    or s[y + i * lr2][x + i * lr1] == "#"
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == "*":
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = "*"
                    break


def check_row(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W or s[y][x + i * lr] == "#":
                break
            if s[y][x + i * lr] == "*":
                for j in range(1 + i):
                    s[y][x + j * lr] = "*"
                break


def check_column(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H or s[y + i * lr][x] == "#":
                break
            if s[y + i * lr][x] == "*":
                for j in range(1 + i):
                    s[y + j * lr][x] = "*"
                break


X, Y = None, None
for y in range(H):
    for x in range(W):
        if s[y][x] == "!":
            X = x
            Y = y
            break

s[Y][X] = "*"
check_row(X, Y, s)
check_column(X, Y, s)
check_diagonal(X, Y, s)

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()



#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        char[][] grid = new char[h][w];
        int targetY = -1;
        int targetX = -1;
        
        for (int i = 0; i < h; i++) {
            String line = sc.next();
            grid[i] = line.toCharArray();
            for (int j = 0; j < w; j++) {
                if (grid[i][j] == '!') {
                    targetY = i;
                    targetX = j;
                    grid[i][j] = '*';
                }
            }
        }
        
        int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        for (int i = 0; i < 8; i++) {
            List<int[]> path = new ArrayList<>();
            int ny = targetY + dy[i];
            int nx = targetX + dx[i];
            
            while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                if (grid[ny][nx] == '.') {
                    path.add(new int[]{ny, nx});
                } else if (grid[ny][nx] == '*') {
                    for (int[] pos : path) {
                        grid[pos[0]][pos[1]] = '*';
                    }
                    break;
                } else {
                    break;
                }
                ny += dy[i];
                nx += dx[i];
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        sc.close();
    }
}



いびつなひとりリバーシ
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int n = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
        
        for (int k = 0; k < n; k++) {
            int targetY = sc.nextInt();
            int targetX = sc.nextInt();
            grid[targetY][targetX] = '*';
            
            for (int i = 0; i < 8; i++) {
                List<int[]> path = new ArrayList<>();
                int ny = targetY + dy[i];
                int nx = targetX + dx[i];
                
                while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                    if (grid[ny][nx] == '.') {
                        path.add(new int[]{ny, nx});
                    } else if (grid[ny][nx] == '*') {
                        for (int[] pos : path) {
                            grid[pos[0]][pos[1]] = '*';
                        }
                        break;
                    } else {
                        break;
                    }
                    ny += dy[i];
                    nx += dx[i];
                }
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        sc.close();
    }
}



#python
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    h = int(input_data[0])
    w = int(input_data[1])
    n = int(input_data[2])
    
    grid = [list(row) for row in input_data[3:3+h]]
    
    moves = []
    idx = 3 + h
    for _ in range(n):
        y = int(input_data[idx])
        x = int(input_data[idx+1])
        moves.append((y, x))
        idx += 2
        
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for target_y, target_x in moves:
        grid[target_y][target_x] = '*'
        
        for i in range(8):
            path = []
            ny, nx = target_y + dy[i], target_x + dx[i]
            
            while 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == '.':
                    path.append((ny, nx))
                elif grid[ny][nx] == '*':
                    for y, x in path:
                        grid[y][x] = '*'
                    break
                else: # '#' 
                    break
                ny += dy[i]
                nx += dx[i]
                
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    solve()




#ans from paiza

H, W, N = map(int, input().split())
s = [list(input()) for _ in range(H)]
points = [list(map(int, input().split())) for _ in range(N)]


def check_diagonal(x, y, s):
    for lr1 in range(-1, 2, 2):
        for lr2 in range(-1, 2, 2):
            i = 0
            while True:
                i += 1
                if (
                    x + i * lr1 < 0
                    or x + i * lr1 >= W
                    or y + i * lr2 < 0
                    or y + i * lr2 >= H
                ):
                    break
                if s[y + i * lr2][x + i * lr1] == "*":
                    for j in range(1 + i):
                        s[y + j * lr2][x + j * lr1] = "*"
                    break
                if s[y + i * lr2][x + i * lr1] == "#":
                    break


def check_row(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if x + i * lr < 0 or x + i * lr >= W:
                break
            if s[y][x + i * lr] == "*":
                for j in range(1 + i):
                    s[y][x + j * lr] = "*"
                break
            if s[y][x + i * lr] == "#":
                break


def check_column(x, y, s):
    for lr in range(-1, 2, 2):
        i = 0
        while True:
            i += 1
            if y + i * lr < 0 or y + i * lr >= H:
                break
            if s[y + i * lr][x] == "*":
                for j in range(1 + i):
                    s[y + j * lr][x] = "*"
                break
            if s[y + i * lr][x] == "#":
                break


for y, x in points:
    s[y][x] = "*"
    check_row(x, y, s)
    check_column(x, y, s)
    check_diagonal(x, y, s)

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()





「いびつなリバーシ対戦（２人） Python3編」
import sys

def solve():
    data = sys.stdin.read().split()
    h, w, n = int(data[0]), int(data[1]), int(data[2])
    idx = 3
    grid = [list(data[idx + i]) for i in range(h)]
    idx += h

    moves = []
    for _ in range(n):
        ya, xa, yb, xb = map(int, data[idx:idx+4])
        moves.append(((ya, xa), (yb, xb)))
        idx += 4

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    def process_turn(y, x, player_char):
        grid[y][x] = player_char

        for i in range(8):
            path = []
            ny, nx = y + dy[i], x + dx[i]
            while 0 <= ny < h and 0 <= nx < w:
                cell = grid[ny][nx]
                if cell == '#':
                    break 
                if cell == player_char:
                    for py, px in path:
                        grid[py][px] = player_char
                    break
                path.append((ny, nx))
                ny += dy[i]
                nx += dx[i]
            

    for (ya, xa), (yb, xb) in moves:
        process_turn(ya, xa, 'A')
        process_turn(yb, xb, 'B')

    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    solve()








「いびつなリバーシ対戦 Python3編」


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    h = int(input_data[ptr]); ptr += 1
    w = int(input_data[ptr]); ptr += 1
    n_players = int(input_data[ptr]); ptr += 1
    n_turns = int(input_data[ptr]); ptr += 1
    
    grid = []
    for _ in range(h):
        grid.append(list(input_data[ptr]))
        ptr += 1
        
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for _ in range(n_turns):
        p_id = input_data[ptr]; ptr += 1
        y = int(input_data[ptr]); ptr += 1
        x = int(input_data[ptr]); ptr += 1
        
        # 放置玩家石子
        grid[y][x] = p_id
        
        # 檢查八個方向
        for i in range(8):
            path = []
            ny, nx = y + dy[i], x + dx[i]
            while 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == '#':
                    break
                elif grid[ny][nx] != p_id:
                    path.append((ny, nx))
                else:
                    for py, px in path:
                        grid[py][px] = p_id
                    break
                
                ny += dy[i]
                nx += dx[i]
                
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    solve()