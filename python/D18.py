マップからの座標取得 Java編

#Q1

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(line));
        
        int n1 = Integer.parseInt(line[0]);
        int n2 = Integer.parseInt(line[1]);
        
        // System.out.println(n1);
        // System.out.println(n2);
        
        for (int i =0; i< n1 ; i++){
            String next = sc.next();
            // System.out.println(next);
            for (int j = 0; j< n2; j++){
                if (next.charAt(j) == '#'){
                    System.out.println(i + " " + j);
                }
            }
        }
    }
}



#python

first, second = map(int, input().split())
# print(first)
# print(second)

for i in range(first):
    strs = input()
    # print(strs)
    for c in range(second):
        # print(strs[c])
        if strs[c] == "#":
            print(i, c)


#ans from paiza
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            print(y, x)





下記の問題をプログラミングしてみよう！
開始時点の y , x 座標 と移動の回数 N が与えられます。
続く N 行で移動の方角 d_1 ... d_N が与えられるので、与えられた順に移動をしたときの各移動後の y , x 座標 を答えてください。

ただし、図の通り、上側（ y 軸の負の向き）を北とします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。



#PYTHON
Y, X, directions = map(int, input().split())
Y, X, directions = map(int, input().split())
# print(Y)
# print(X)
# print(directions)

tem = []
# now at (0, 0)
for i in range(directions):
    direction = input()
    tem += direction
    # print(direction)
    
for u in tem:
    # print(u)
    if u == 'N':
        #WE SHOULD MOVE Y min
        Y -= 1
        print(Y, X)
    elif u == 'W':
        X -= 1
        print(Y, X)
    elif u == 'E':
        #WE SHOULD MOVE Y min
        X += 1
        print(Y, X)
    else :
        Y += 1
        print(Y, X)




#JAVA


import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(line));
        
        int n1 = Integer.parseInt(line[0]);
        int n2 = Integer.parseInt(line[1]);
        int directions = Integer.parseInt(line[2]);
        
        // System.out.println(n1);
        // System.out.println(n2);
        String tem[] = new String[directions];
        
        for (int i =0; i< directions ; i++){
            String direction = sc.next();
            // System.out.println(direction);
            tem[i] = direction;
        }
        
        
        for (String c: tem){
            // System.out.println(c);
            if (c.equals("N")){
                n1 -= 1;
                System.out.println(n1 +" "+ n2);
            }else if (c.equals("W")){
                n2 -= 1;
                System.out.println(n1 +" "+ n2);
            }else if (c.equals("E")){
                n2 += 1;
                System.out.println(n1 +" "+ n2);
            }else {
                n1 += 1;
                System.out.println(n1 +" "+ n2);
            }
        }
    }
}

// (direction.charAt(i) == 'S')

#ans from paiza
y, x, n = map(int, input().split())

for _ in range(n):
    direction = input()

    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1

    print(y, x)