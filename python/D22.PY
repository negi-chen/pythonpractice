「移動が可能かの判定・方向」

# 1. read all
allin = input().split()
h = int(allin[0])
w = int(allin[1])
sy = int(allin[2])
sx = int(allin[3])
dr = allin[4]          # directions (N, S, E, W)
leftorright = allin[5] # check (L, R)

# 2. read map
grid = []
for i in range(h):
    grid.append(input().strip())

# assume the ans's direction is the same
next_y = sy
next_x = sx

# 3. according to the resources to turn the direction
if dr == "N":
    if leftorright == "R":
        next_x += 1
    elif leftorright == "L":
        next_x -= 1
        
elif dr == "E":
    if leftorright == "R":
        next_y += 1
    elif leftorright == "L":
        next_y -= 1
        
elif dr == "S":
    if leftorright == "R":
        next_x -= 1
    elif leftorright == "L":
        next_x += 1
        
elif dr == "W":
    if leftorright == "R":
        next_y -= 1
    elif leftorright == "L":
        next_y += 1

#bsically set as No
answer = "No"

# check whether out of boundary
if 0 <= next_y < h and 0 <= next_x < w:
    # check if it's whether it's # or not 
    if grid[next_y][next_x] != '#':
        answer = "Yes"

print(answer)


#ans from paiza
h, w, sy, sx, d, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = directions.index(d)

if m == "L":
    now = (3 + now) % 4
else:
    now = (1 + now) % 4


if directions[now] == "N":
    sy -= 1
elif directions[now] == "E":
    sx += 1
elif directions[now] == "S":
    sy += 1
elif directions[now] == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")


#java 
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        
        int di1 = Integer.parseInt(line[0]); // H 
        int di2 = Integer.parseInt(line[1]); // W 
        int anc3 = Integer.parseInt(line[2]); // sy Y
        int anc4 = Integer.parseInt(line[3]); // sx X
        String dr = line[4];                 // directions (N, S, E, W)
        String leftorright = line[5];        // turn to left or right (L, R)
        
        String[] grid = new String[di1];
        for (int k = 0; k < di1; k++) {
            grid[k] = sc.next();
        }

        String ans = "No";
        
        //for two loops
        for (int i = 0; i < di1; i++) {
            for (int j = 0; j < di2; j++) {
                if (anc3 == i && anc4 == j) {
                    
                    //first checkdirections and then move left or right
                    if (dr.equals("N")) {
                        if (leftorright.equals("R")) {      
                            if (j + 1 < di2 && grid[i].charAt(j + 1) != '#') ans = "Yes";
                        } else if (leftorright.equals("L")) { 
                            if (j - 1 >= 0 && grid[i].charAt(j - 1) != '#') ans = "Yes";
                        }
                    } 
                    else if (dr.equals("E")) {
                        if (leftorright.equals("R")) {      
                            if (i + 1 < di1 && grid[i + 1].charAt(j) != '#') ans = "Yes";
                        } else if (leftorright.equals("L")) { 
                            if (i - 1 >= 0 && grid[i - 1].charAt(j) != '#') ans = "Yes";
                        }
                    } 
                    else if (dr.equals("S")) {
                        if (leftorright.equals("R")) {      
                            if (j - 1 >= 0 && grid[i].charAt(j - 1) != '#') ans = "Yes";
                        } else if (leftorright.equals("L")) { 
                            if (j + 1 < di2 && grid[i].charAt(j + 1) != '#') ans = "Yes";
                        }
                    } 
                    else if (dr.equals("W")) {
                        if (leftorright.equals("R")) {      
                            if (i - 1 >= 0 && grid[i - 1].charAt(j) != '#') ans = "Yes";
                        } else if (leftorright.equals("L")) {                             if (i + 1 < di1 && grid[i + 1].charAt(j) != '#') ans = "Yes";
                        }
                    }
                    
                }
            }
        }
        System.out.println(ans);
    }
}



マップの行数 H と列数 W , 現在の座標 sy , sx , 移動の回数 N が与えられます。
続けて、障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列 のマップ S_1 ... S_H と N 回の移動の向き d_1 ... d_N が与えられます。

移動者ははじめ北を向いています。移動者は、1 回の移動で次の行動を行います。

「移動の向きに方向転換したのち、1 マス進む。」

各移動が可能である場合、移動後の y , x 座標を出力してください。
移動が可能でない場合、移動後の座標を出力する代わりに "Stop" を出力して、以降の移動を打ち切ってください。

各移動が可能であるということは、以下の図の通り
「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

# 1. Read
allin = input().split()
h = int(allin[0])
w = int(allin[1])
y = int(allin[2])  # current y
x = int(allin[3])  # current x
n = int(allin[4])  # n

# 2. read input
grid = []
for i in range(h):
    grid.append(input().strip())

# 3. defult direction = N 
dr = "N"

# 4. repeat n time
for i in range(n):
    leftor = input().strip()  # read each l and r
    
    next_y = y
    next_x = x
    
    if dr == 'N':
        if leftor == 'R':
            next_x += 1
            next_dr = 'E'
        elif leftor == 'L':
            next_x -= 1
            next_dr = 'W'
            
    elif dr == 'W':
        if leftor == 'R':
            next_y -= 1
            next_dr = 'N'
        elif leftor == 'L':
            next_y += 1
            next_dr = 'S'
            
    elif dr == 'E':
        if leftor == 'R':
            next_y += 1
            next_dr = 'S'
        elif leftor == 'L':
            next_y -= 1
            next_dr = 'N'
            
    elif dr == 'S':
        if leftor == 'R':
            next_x -= 1
            next_dr = 'W'
        elif leftor == 'L':
            next_x += 1
            next_dr = 'E'


    if 0 <= next_y < h and 0 <= next_x < w and grid[next_y][next_x] != '#':
        y = next_y
        x = next_x
        dr = next_dr
        print(y, x)
    else:
        print("Stop")
        break


#java

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int w = sc.nextInt();
        int y = sc.nextInt();
        int x = sc.nextInt();
        int n = sc.nextInt();
        
        String[] grid = new String[h];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next();
        }

        String dr = "N";
        
        for (int i = 0; i < n; i++) {
            String leftor = sc.next();
            
            int nextY = y;
            int nextX = x;
            String nextDr = dr;
            
            if (dr.equals("N")) {
                if (leftor.equals("R")) {
                    nextX += 1;
                    nextDr = "E";
                } else if (leftor.equals("L")) {
                    nextX -= 1;
                    nextDr = "W";
                }
            } else if (dr.equals("W")) {
                if (leftor.equals("R")) {
                    nextY -= 1;
                    nextDr = "N";
                } else if (leftor.equals("L")) {
                    nextY += 1;
                    nextDr = "S";
                }
            } else if (dr.equals("E")) {
                if (leftor.equals("R")) {
                    nextY += 1;
                    nextDr = "S";
                } else if (leftor.equals("L")) {
                    nextY -= 1;
                    nextDr = "N";
                }
            } else if (dr.equals("S")) {
                if (leftor.equals("R")) {
                    nextX -= 1;
                    nextDr = "W";
                } else if (leftor.equals("L")) {
                    nextX += 1;
                    nextDr = "E";
                }
            }
            

            if (nextY >= 0 && nextY < h && nextX >= 0 && nextX < w && grid[nextY].charAt(nextX) != '#') {
                y = nextY;
                x = nextX;
                dr = nextDr;
                System.out.println(y + " " + x);
            } else {
                System.out.println("Stop");
                break; 
            }
        }
        
        sc.close();
    }
}


#ans from paiza
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d = input()
    if d == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    if directions[now] == "N":
        sy -= 1
    elif directions[now] == "E":
        sx += 1
    elif directions[now] == "S":
        sy += 1
    elif directions[now] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
        print("Stop")
        break
    else:
        print(sy, sx)



マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy, sx, 移動の回数 N が与えられます。
続けて、 N 回の移動の向き d_1 ... d_N と移動するマス数 l_1 ... l_N が与えられます。

プレイヤーははじめ北を向いています。

各移動が可能である場合、移動後の y , x 座標 を出力してください。
移動が可能でない場合(移動しきれない場合)、移動できるところまで移動した後の座標を出力した後に "Stop" を出力して、以降の移動を打ち切ってください。

各移動が可能であるということは、以下の図の通り
「今いるマスから移動先のマスまでに障害物がない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


#pthon
# 1. Read
h, w, sy, sx, n= map(int, input().split())

grid = [input().strip() for _ in range(h)]

y, x = sy, sx
dr = 'N' 
stopped = False

# 4. n times
for i in range(n):
    if stopped:
        break
        
    # L or R
    d, l_str = input().split()
    l = int(l_str)
    
    if dr == 'N':
        dr = 'W' if d == 'L' else 'E'
    elif dr == 'E':
        dr = 'N' if d == 'L' else 'S'
    elif dr == 'S':
        dr = 'E' if d == 'L' else 'W'
    elif dr == 'W':
        dr = 'S' if d == 'L' else 'N'
        
    for step in range(l):
        next_y, next_x = y, x
        if dr == 'N': next_y -= 1
        elif dr == 'E': next_x += 1
        elif dr == 'S': next_y += 1
        elif dr == 'W': next_x -= 1
        
        if 0 <= next_y < h and 0 <= next_x < w and grid[next_y][next_x] != '#':
            y, x = next_y, next_x  
        else:
            print(y, x)
            print("Stop")
            stopped = True
            break  

    if not stopped:
        print(y, x)



#ANS FROM PAIZA
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            if directions[now] == "N":
                sy += 1
            elif directions[now] == "E":
                sx -= 1
            elif directions[now] == "S":
                sy -= 1
            elif directions[now] == "W":
                sx += 1
            break

    print(sy, sx)
    if flag:
        print("Stop")
        break



#JAVA
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int y = sc.nextInt();
        int x = sc.nextInt();
        int n = sc.nextInt();
        
        String[] grid = new String[h];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next();
        }
        
        
        String dr = "N"; 
        boolean stopped = false;

        for (int i = 0; i < n; i++) {
            String d = sc.next();
            int l = sc.nextInt();
            
            if (stopped) continue;
            
            if (dr.equals("N")) {
                dr = d.equals("L") ? "W" : "E";
            } else if (dr.equals("E")) {
                dr = d.equals("L") ? "N" : "S";
            } else if (dr.equals("S")) {
                dr = d.equals("L") ? "E" : "W";
            } else if (dr.equals("W")) {
                dr = d.equals("L") ? "S" : "N";
            }
            
            for (int step = 0; step < l; step++) {
                int nextY = y;
                int nextX = x;
                
                if (dr.equals("N")) nextY -= 1;
                else if (dr.equals("E")) nextX += 1;
                else if (dr.equals("S")) nextY += 1;
                else if (dr.equals("W")) nextX -= 1;
                
                if (nextY >= 0 && nextY < h && nextX >= 0 && nextX < w && grid[nextY].charAt(nextX) != '#') {
                    y = nextY;
                    x = nextX;
                } else {
                    System.out.println(y + " " + x);
                    System.out.println("Stop");
                    stopped = true;
                    break;
                }
            }
            
            if (!stopped) {
                System.out.println(y + " " + x);
            }
        }
        sc.close();
    }
}


マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 移動の回数 N が与えられます。
続けて N 回の移動の向き d_1 ... d_N と移動するマス数 l_1...l_N が与えられます。

はじめは北を向いています。

各移動が可能である場合、スタート位置を含む移動の際に通ったマップのマスを '*' に変更してください。
移動が可能でない場合、障害物やマップの端までできる限り移動をして通ったマップのマスを '*' に変更したのち、以降の移動を打ち切ってください。

移動が終了した時のマップを出力してください。

移動可能であるということは、以下の図の通り
「今いるマスから移動先のマスまでに障害物がない かつ 移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w, sy, sx, n= map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
y, x = sy, sx
grid[y][x] = '*'
dr = 'N'
stopped = False

for _ in range(n):
    if stopped:
        break
    
    d, l_str = input().split()
    l = int(l_str)
    
    if dr == 'N':
        dr = 'W' if d == 'L' else 'E'
    elif dr == 'E':
        dr = 'N' if d == 'L' else 'S'
    elif dr == 'S':
        dr = 'E' if d == 'L' else 'W'
    elif dr == 'W':
        dr = 'S' if d == 'L' else 'N'
        
    for _ in range(l):
        next_y, next_x = y, x
        if dr == 'N': next_y -= 1
        elif dr == 'E': next_x += 1
        elif dr == 'S': next_y += 1
        elif dr == 'W': next_x -= 1
        
        if 0 <= next_y < h and 0 <= next_x < w and grid[next_y][next_x] != '#':
            y, x = next_y, next_x
            grid[y][x] = '*'
        else:
            stopped = True
            break

for row in grid:
    print("".join(row))


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int y = sc.nextInt();
        int x = sc.nextInt();
        int n = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        grid[y][x] = '*';
        String dr = "N";
        boolean stopped = false;
        
        for (int i = 0; i < n; i++) {
            String d = sc.next();
            int l = sc.nextInt();
            
            if (stopped) continue;
            
            if (dr.equals("N")) {
                dr = d.equals("L") ? "W" : "E";
            } else if (dr.equals("E")) {
                dr = d.equals("L") ? "N" : "S";
            } else if (dr.equals("S")) {
                dr = d.equals("L") ? "E" : "W";
            } else if (dr.equals("W")) {
                dr = d.equals("L") ? "S" : "N";
            }
            
            for (int step = 0; step < l; step++) {
                int nextY = y;
                int nextX = x;
                
                if (dr.equals("N")) nextY -= 1;
                else if (dr.equals("E")) nextX += 1;
                else if (dr.equals("S")) nextY += 1;
                else if (dr.equals("W")) nextX -= 1;
                
                if (nextY >= 0 && nextY < h && nextX >= 0 && nextX < w && grid[nextY][nextX] != '#') {
                    y = nextY;
                    x = nextX;
                    grid[y][x] = '*';
                } else {
                    stopped = true;
                    break;
                }
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        
        sc.close();
    }
}


#ANS FROM PAIZA
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0
s[sy][sx] = "*"

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            break
        else:
            s[sy][sx] = "*"

    if flag:
        break

for y in range(int(h)):
    print("".join(s[y]))


へびがマップ上を移動していきます。
マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 方向転換の回数 N が与えられます。
続けて N 回の方向転換する時刻 t_1 ... t_N , 転換する向き d_1 ... d_N が与えられます。

へびははじめ、北を向いています。

時刻 0 から 99 までの間、へびは各時刻に次の行動を最大 100 回とります。

・ 方向転換をおこなう時刻の場合、指定の向きに方向転換したのち 1 マス身体を伸ばす。
・ そうでない時は移動が可能な場合に限り、今向いている方向に 1 マス身体を伸ばす。

各移動が可能であるということは、
「移動先のマスに障害物がない かつ 移動先がマップの範囲外でない」
ということを意味します。

各移動が可能である場合、各移動が終了した時の y , x 座標を出力してください。
移動が可能でない場合、"Stop" を出力して以降の移動を打ち切ってください。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

移動の一例をあげます。例えば次のような入力が与えられた時は図のような移動になります。


h, w, sy, sx, n = map(int, input().split())
grid = [input().strip() for _ in range(h)]
# print(grid)

#this is maps
turns = {}
for _ in range(int(n)):
    t_i, d_i = input().split()
    turns[int(t_i)] = d_i
    
# print(turns)
directions = ["N","E","S","W"]
now = 0

y, x = sy, sx

for i in range(100):
    if i in turns:
        # print(turns[i])
        d_i = turns[i]
        if d_i == "L": #heres idea is that north east south west (0 1 2 3) 
        #here will be north west south east north
            now = (now + 3) % 4 #because left so here is saying we want number be less than one  
        else: #and here is like north east south west
            now = (now + 1) % 4  
    
    
    if directions[now] == "N":
        y -= 1
    elif directions[now] == "E":
        x += 1
    elif directions[now] == "S":
        y += 1
    elif directions[now] == "W":
        x -= 1
          
                
    
    if x < 0 or x >= int(w) or y < 0 or y >= int(h) or grid[y][x] == "#":
        print("Stop")
        break
    else:
        print(y, x)
       

#ANS FROM PAIZA
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
time_lr = [input().split() for _ in range(int(n))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now_direction = 0
time_index = 0


for t_now in range(100):
    if str(t_now) == time_lr[time_index][0]:
        d = time_lr[time_index][1]
        time_index += 1
        if d == "L":
            now_direction = (3 + now_direction) % 4
        else:
            now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        sy -= 1
    elif directions[now_direction] == "E":
        sx += 1
    elif directions[now_direction] == "S":
        sy += 1
    elif directions[now_direction] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
        print("Stop")
        break
    else:
        print(sy, sx)



import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int y = sc.nextInt();
        int x = sc.nextInt();
        int n = sc.nextInt();
        
        String[] grid = new String[h];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next();
        }
        // System.out.println(grid);
        
        HashMap<Integer, String> turns = new HashMap<>();
        for (int i = 0; i < n; i++) {
            turns.put(sc.nextInt(), sc.next());
        }
        
        String[] directions = {"N", "E", "S", "W"};
        int now = 0;
        
        
        
       for (int t = 0; t < 100; t++) {
            if (turns.containsKey(t)) {
                String d = turns.get(t);
                if (d.equals("L")) {
                    now = (now + 3) % 4;
                } else {
                    now = (now + 1) % 4;
                }
            }
            
            if (directions[now].equals("N")) y--;
            else if (directions[now].equals("E")) x++;
            else if (directions[now].equals("S")) y++;
            else if (directions[now].equals("W")) x--;
            
            if ( x < 0 || x >= w || y < 0 || y >= h || grid[y].charAt(x) == '#') {
                System.out.println("Stop");
                break;
            } else {
                System.out.println(y + " " + x);
            }
        }
        sc.close();
    }
}





FINAL 
マップ上をへびが移動していきます。
マップの行数 H と列数 W ,障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 方向転換の回数 N が与えられます。
続けて N 回の方向転換をおこなう時刻 t_1 ... t_N, 転換する向き d_1 ... d_N が与えられます。

へびははじめは北を向いています。

へびは進む先のマスに自分の身体や障害物がない時に移動ができます。
時刻 0 から 99 までの間、へびは各時刻に次の行動を最大 100 回繰り返します。

・ 方向転換をおこなう時刻の場合、指定の向きに方向転換したのち １ マス身体を伸ばす。そうでない時は、今向いている方向に １ マス身体を伸ばす。

時刻が 99 の時の行動を終えるか、移動できなくなった時、移動を終了します。
移動終了時にへびの体のあるマスを '*' にしたマップを出力してください。

移動が可能であるということは、
「移動先のマスに自分の身体や障害物がない かつ 移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

移動の一例をあげます。例えば次のような入力が与えられた時は図のような移動になります。
図は、時刻 T の行動前の状態を表しています。




import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int y = sc.nextInt();
        int x = sc.nextInt();
        int n = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        // System.out.println(grid);
        
        HashMap<Integer, String> turns = new HashMap<>();
        for (int i = 0; i < n; i++) {
            turns.put(sc.nextInt(), sc.next());
        }
        
        String[] directions = {"N", "E", "S", "W"};
        int now = 0;
        
        grid[y][x] = '*';
       for (int t = 0; t < 100; t++) {
            if (turns.containsKey(t)) {
                String d = turns.get(t);
                if (d.equals("L")) {
                    now = (now + 3) % 4;
                } else {
                    now = (now + 1) % 4;
                }
            }
            
            if (directions[now].equals("N")) {
                y--;
            } else if (directions[now].equals("E")){
                x++;
            } else if (directions[now].equals("S")) {
                y++;
            } else if (directions[now].equals("W")) {
                x--;
            }
            if ( x < 0 || x >= w || y < 0 || y >= h || grid[y][x] == '#'|| grid[y][x]=='*') {
                break;
            } 
            grid[y][x] ='*';
        }
        
        for (int z = 0; z < h ; z++) {
            System.out.println(new String(grid[z]));
        }
        sc.close();
    }
}


#python
h, w, y, x, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
# print(grid)

#this is maps
turns = {}
for _ in range(int(n)):
    t_i, d_i = input().split()
    turns[int(t_i)] = d_i
    
# print(turns)
directions = ["N","E","S","W"]
now = 0

grid[y][x] = "*"


for i in range(100):
    if i in turns:
        # print(turns[i])
        d_i = turns[i]
        if d_i == "L": #heres idea is that north east south west (0 1 2 3) 
        #here will be north west south east north
            now = (now + 3) % 4 #because left so here is saying we want number be less than one  
        else: #and here is like north east south west
            now = (now + 1) % 4  
    
    
    if directions[now] == "N":
        y -= 1
    elif directions[now] == "E":
        x += 1
    elif directions[now] == "S":
        y += 1
    elif directions[now] == "W":
        x -= 1
          
                
    
    if x < 0 or x >= int(w) or y < 0 or y >= int(h) or grid[y][x] == "#" or grid[y][x] =="*":
        break
    grid[y][x] = "*"
        
        
for row in grid:
    print("".join(row))
    

#ans from paiza
h, w, sy, sx, n = map(int, input().split())
s = [list(input()) for _ in range(int(h))]
time_lr = [input().split() for _ in range(int(n))]
directions = ["N", "E", "S", "W"]
now_direction = 0
time_index = 0
s[sy][sx] = "*"

for t_now in range(100):
    if time_index < n and str(t_now) == time_lr[time_index][0]:
        d = time_lr[time_index][1]
        time_index += 1
        if d == "L":
            now_direction = (3 + now_direction) % 4
        else:
            now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        sy -= 1
    elif directions[now_direction] == "E":
        sx += 1
    elif directions[now_direction] == "S":
        sy += 1
    elif directions[now_direction] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] != ".":
        break
    else:
        s[sy][sx] = "*"

for y in range(int(h)):
    for x in range(int(w)):
        print(s[y][x], end="")
    print()