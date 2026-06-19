入力される値
Y X D       
d

・ 1 行目には、開始時点の y , x 座標を表す Y , X,　現在の向いている方角を表す文字 D が与えられます。
・ 2 行目には、移動の向きを表す文字 d が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
1 行での出力

・ 移動した後の y , x 座標を出力してください。
y x

Y, X, directions = input().split()
# print(Y)
# print(X)
# print(directions)

Y= int(Y)
X= int(X)

leftor = input()
# print(leftor)
    
# for u in tem:
#     # print(u)
if directions == 'N':
    #WE SHOULD MOVE N THEN L R
    if leftor == 'R':
        X = X + 1
    elif leftor == 'L':
        X = X - 1
elif directions == 'W':
    if leftor == 'R':
        Y = Y-1
    elif leftor == 'L':
        Y = Y+1
elif directions == 'E':
    #WE SHOULD MOVE Y min
    if leftor == 'R':
        Y = Y+1
    elif leftor == 'L':
        Y = Y-1
else :
    if leftor == 'R':
        X= X - 1
    elif leftor == 'L':
        X= X + 1
    
print(Y, X)
    


#python ans from paiza
y, x, now_direction = input().split()
y = int(y)
x = int(x)
d = input()
lr = 1

if d == "L":
    lr = -1

if now_direction == "N":
    x += lr
elif now_direction == "E":
    y += lr
elif now_direction == "S":
    x -= lr
elif now_direction == "W":
    y -= lr

print(y, x)



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(line));
        
        int n1 = Integer.parseInt(line[0]);
        int n2 = Integer.parseInt(line[1]);
        String directions = line[2];
        
        // System.out.println(n1);
        // System.out.println(n2);
        String leftor = sc.next();
        
        if (directions.equals("N")){
            if(leftor.equals("R")){
                n2 += 1;
            }else if(leftor.equals("L")){
                n2 -=1;
            }
        }else if (directions.equals("W")){
            if(leftor.equals("R")){
                n1 -= 1;
            }else if(leftor.equals("L")){
                n1 +=1;
            }
        }else if (directions.equals("E")){
            if(leftor.equals("R")){
                n1 += 1;
            }else if(leftor.equals("L")){
                n1 -=1;
            }
        }else {
            if(leftor.equals("R")){
                n2 -= 1;
            }else if(leftor.equals("L")){
                n2 +=1;
            }
        }
         System.out.println(n1 +" "+ n2);
    }
}


question2
開始時点の x , y 座標と移動の歩数 N が与えられます。
以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。

なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

x, y, steps = map(int, input().split())
# print(x, y)
# print(steps)


dx=[1, 0, -1, 0] #right down left up(0,1,2,3)
dy=[0, 1, 0, -1]

str_len = []
for i in range(1, 101):
    str_len.append(i)
# print(str_len)


#this means we have to have number 
finalsteps = int(steps/2 +1)
#first turn this into wholenumber with int
# print("1. -- the longest steps: --", finalsteps)

for c in range(finalsteps):
    # print(c)#run two times
    # print(" this need to add twice ech directions :",str_len[c])
    currentlen = (str_len[c])
    # i can split the odd and even and then *2
    # first run -> this is 
    #we have four times
    # print("each time :" , x ," and" , y)
    
    if c % 2 == 0: #means this is even(even will go left up)
    #if its even it will run four dir of x and y 
        move = min(steps, currentlen)
        x += dx[0] * move
        y += dy[0] * move
        steps -= move
        if steps <= 0:
            break
        
        move = min(steps, currentlen)
        x += dx[1] * move
        y += dy[1] * move
        steps -= move
        if steps <= 0:
            break
        

    else:
    #if its odd it will also run four dir of x and y
        #means this is odd
        move = min(steps, currentlen)
        x += dx[2] * move
        y += dy[2] * move
        steps -= move
        if steps <= 0:
            break
        
        move = min(steps, currentlen)
        x += dx[3] * move
        y += dy[3] * move
        steps -= move
        if steps <= 0:
            break

print(x, y)





下記の問題をプログラミングしてみよう！
開始時点の x , y 座標と移動の歩数 N が与えられます。
以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。

なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。
入力される値
X Y N


・ 1 行で、開始時点の x , y 座標を表す X , Y, 移動の歩数 N が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
1行での出力

・ 移動を N 歩行った後の x , y 座標を出力してください。
x y


x, y, steps = map(int, input().split())
# print(x, y)
# print(steps)


dx=[1, 0, -1, 0] #right down left up(0,1,2,3)
dy=[0, 1, 0, -1]

str_len = []
for i in range(1, 101):
    str_len.append(i)
# print(str_len)


#this means we have to have number 
finalsteps = int(steps/2 +1)
#first turn this into wholenumber with int
# print("1. -- the longest steps: --", finalsteps)

for c in range(finalsteps):
    # print(c)#run two times
    # print(" this need to add twice ech directions :",str_len[c])
    currentlen = (str_len[c])
    # i can split the odd and even and then *2
    # first run -> this is 
    #we have four times
    # print("each time :" , x ," and" , y)
    
    if c % 2 == 0: #means this is even(even will go left up)
    #if its even it will run four dir of x and y 
        move = min(steps, currentlen)
        x += dx[0] * move
        y += dy[0] * move
        steps -= move
        if steps <= 0:
            break
        
        move = min(steps, currentlen)
        x += dx[1] * move
        y += dy[1] * move
        steps -= move
        if steps <= 0:
            break
        

    else:
    #if its odd it will also run four dir of x and y
        #means this is odd
        move = min(steps, currentlen)
        x += dx[2] * move
        y += dy[2] * move
        steps -= move
        if steps <= 0:
            break
        
        move = min(steps, currentlen)
        x += dx[3] * move
        y += dy[3] * move
        steps -= move
        if steps <= 0:
            break

print(x, y)

    

#ans from paiza
x, y, n = map(int, input().split())
directions = ["E", "S", "W", "N"]
now_direction = 0
count = 0
max_count = 1
first = True


def move(direction, x, y):
    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1
    return (x, y)


for _ in range(n):
    (x, y) = move(directions[now_direction], x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4


print(x, y)



# java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(line));
        
        int x = Integer.parseInt(line[0]);
        int y = Integer.parseInt(line[1]);
        int steps = Integer.parseInt(line[2]);
        
        int k = (int)Math.sqrt(steps);
        
        if (k * (k + 1) > steps) {
        k--;
        }
        
        int baseMove;
        if (k % 2 == 0) {
            baseMove = -(k / 2);
        } else {
            baseMove = (k + 1) / 2;
        }
        x += baseMove;
        y += baseMove;
        
        int [] dx ={1, 0, -1, 0};
        int [] dy ={0, 1, 0, -1};
        
        int remainingSteps = steps - (k * (k + 1));
        // System.out.println(remainingSteps);
        
        int currentLen = k + 1;
        
        if (k % 2 == 0) {
            int moveRight = Math.min(remainingSteps, currentLen);
            x += moveRight;
            remainingSteps -= moveRight;
            
            int moveDown = Math.min(remainingSteps, currentLen);
            y += moveDown;
        } else {
            int moveLeft = Math.min(remainingSteps, currentLen);
            x -= moveLeft;
            remainingSteps -= moveLeft;
            
            int moveUp = Math.min(remainingSteps, currentLen);
            y -= moveUp;
        }
        
        System.out.println(x + " " + y); 
    }
}