裏返せる可能性（縦横）

#python
h, w, targety, targetx = map(int , input().split())

# print(h, w, targety, targetx)

lonstr = []

#for somthing right down and left right

for y in range(h):
    row = []
    for x in range(w):
        if targety == y and x == targetx:
            row.append("!")
        elif x == targetx or y == targety:
            row.append ("*")
        else:
            row.append(".")
    lonstr.append(row)
    # print("1. how we append :" , lonstr)


for i in lonstr:
    print("".join(i))
        



#ans from paiza
H, W, Y, X = map(int, input().split())

for y in range(H):
    for x in range(W):
        if y == Y and x == X:
            print("!", end="")
        elif y == Y or x == X:
            print("*", end="")
        else:
            print(".", end="")
    print()


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int targetx = sc.nextInt();
        int targety = sc.nextInt();
        
        for (int i = 0; i< h ; i++){
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j< w ; j++){
                if (j == targety && i == targetx) {
                    sb.append('!');
                } else if (j == targety || i == targetx) {
                    sb.append('*');
                } else {
                    sb.append('.');
                }
            }
            System.out.println(sb.toString());
            }
        sc.close();
        
    }
}





リバーシの操作（縦横）

h, w, targety, targetx = map(int , input().split())

# print(h, w, targety, targetx)

lonstr = []
for i in range(h):
    row = list(input())
    lonstr.append(row)
    
# print(lonstr[targety][targetx])
ny = targety+1
nx = targetx + 1
my = targety -1
mx = targetx -1
    
path = []    

while nx < w:
    if lonstr[targety][nx] == "*" :
        for py, px in path:
            lonstr[py][px] = "*"
        break

    elif lonstr[targety][nx] == ".":
        path.append((targety, nx))
    nx += 1

path = []  
while ny < h:
    if lonstr[ny][targetx] == "*" :
        for py, px in path:
            lonstr[py][px] = "*"
        break

    elif lonstr[ny][targetx] == ".":
        path.append((ny, targetx))
    ny += 1
    

path = []      
while mx >= 0:
    if lonstr[targety][mx] == "*" :
        for py, px in path:
            lonstr[py][px] = "*"
        break

    elif lonstr[targety][mx] == ".":
        path.append((targety, mx))
    mx -= 1

path = []      
while my >= 0:
    if lonstr[my][targetx] == "*" :
        for py, px in path:
            lonstr[py][px] = "*"
        break

    elif lonstr[my][targetx] == ".":
        path.append((my, targetx))
    my -= 1
    
lonstr[targety][targetx] = "*"
    
    
for i in lonstr:
    print("".join(i))




#ANS FROM PAIZA
H, W, Y, X = map(int, input().split())
s = [list(input()) for _ in range(H)]


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

for y in range(H):
    for x in range(W):
        print(s[y][x], end="")
    print()



#JAVA
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
        
        #UP DOWN AND LEFT RIGHT
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
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



裏返せる可能性（斜め）


import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int targetY = sc.nextInt();
        int targetX = sc.nextInt();
        
        char[][] grid = new char[h][w];
        // for (int i = 0; i < h; i++) {
        //     grid[i] = sc.next().toCharArray();
        // }
        
        for (int i = 0; i< h ; i++){
            for (int j = 0; j< w ; j++){
                grid[i][j] = '.';
            }
        }
        
        
        grid[targetY][targetX] = '!';
        
        //UP DOWN AND LEFT RIGHT
        int[] dy = {-1, -1, 1, 1};
        int[] dx = {-1, 1, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            List<int[]> path = new ArrayList<>();
            int ny = targetY + dy[i];
            int nx = targetX + dx[i];
            
            while (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                grid[ny][nx] = '*';
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


import sys

def main():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    h = int(input_data[0])
    w = int(input_data[1])
    target_y = int(input_data[2])
    target_x = int(input_data[3])
    
    grid = [['.' for _ in range(w)] for _ in range(h)]
    
    grid[target_y][target_x] = '!'
    
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]
    
    for i in range(4):
        ny = target_y + dy[i]
        nx = target_x + dx[i]
        
        while 0 <= ny < h and 0 <= nx < w:
            grid[ny][nx] = '*'  
            ny += dy[i]         
            nx += dx[i]
            
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    main()




#ans from paiza
H, W, Y, X = map(int, input().split())

for i in range(H):
    for j in range(W):
        if i == Y and j == X:
            print("!", end="")
        elif abs(i - Y) == abs(j - X):
            print("*", end="")
        else:
            print(".", end="")
    print()