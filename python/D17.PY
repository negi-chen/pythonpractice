question1
行数 H , 列数 W の盤面があり、盤面の各マスには文字が 1 つだけ書かれています。
盤面が与えられるので、「左右のマスが "#" 」であるようなマスの座標を全て出力してください。

ただし、左端のマスの場合は「右のマスが "#" 」であれば、右端のマスの場合は「左のマスが "#" 」であれば条件を満たすものとします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


ints = input().split()

first = int(ints[0])
second = int(ints[1])

print(first)
print(second)

strs =[]

#so for read we only need to have one loop 
for i in range(first):
    nexts = input()
    strs.append(nexts)
        
print(strs)
        
# then we loop to fin the target
for row in range(first):
    # print(row)
    for column in range(second):
        # print(strs[row][column])
        
        #situation one+
        if column == 0:
            # here we check the right is fine
            if strs[row][column + 1] == "#":
                print("check",row, column)
        
        #situation two+
        elif column == second -1:
            if strs[row][column - 1] == "#":
                print(row, column)
                
        #situation three+
        else:
            if strs[row][column-1] =="#" and strs[row][column+1] =="#":
                print(row, column)
            # print(second -1)
            #can i print somthing like if that row have # then ill print the all the columns in the row other then that 


#python ans from paiza
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                print(y, x)



#java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] lines= sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(lines));
        
        int h = Integer.parseInt(lines[0]);
        int w = Integer.parseInt(lines[1]);
        
        char[][]board = new char[h][w];
        
        for(int i =0; i< h; i++){
            String dott = sc.next();
            for(int j =0; j< w; j++){
                board[i][j] = dott.charAt(j);
                // System.out.println(board[i][j]); //check each char
            }
        }
            
            
        for(int i =0; i< h; i++){
            for(int j =0; j< w; j++){
                if (j == 0){
                    if(board[i][j+1] == '#'){
                        System.out.println(i+ " " +j);
                    }
                }else if(j == w-1){
                    if(board[i][j-1] == '#'){
                    System.out.println(i+ " " +j);
                    }
                }else{
                    if(board[i][j-1] == '#' && board[i][j+1] == '#'){
                    System.out.println(i+ " " +j);
                    }
                }
            }
        } 
    }
}



マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ... S_H が与えられるので、
上下のマスがどちらも '#' であるようなマスの y , x 座標 を答えてください。

ただし、上端のマスの場合は「下のマスが '#'」であれば、下端のマスの場合は「上のマスが '#'」であれば条件を満たすものとします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

# paython 
ints = input().split()

first = int(ints[0])
second = int(ints[1])

# print(first)
# print(second)

strs =[]

#so for read we only need to have one loop 
for i in range(first):
    nexts = input()
    strs.append(nexts)
        
# print(strs)
        
# then we loop to fin the target
for row in range(first):
    # print(row)
    for column in range(second):
        # print(strs[row][column])
        
        #situation one+
        if row == 0:
            # here we check the down is fine
            if strs[row + 1][column] == "#":
                print(row, column)
        
        #situation two+
        elif row == first -1:
            if strs[row-1][column] == "#":
                print(row, column)
                
        #situation three+
        else:
            if strs[row+1][column] =="#" and strs[row-1][column] =="#":
                print(row, column)
            # print(second -1)
            #can i print somthing like if that row have # then ill print the all the columns in the row other then that 


#ans from paiza
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                print(y, x)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] lines= sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(lines));
        
        int h = Integer.parseInt(lines[0]);
        int w = Integer.parseInt(lines[1]);
        
        char[][]board = new char[h][w];
        
        for(int i =0; i< h; i++){
            String dott = sc.next();
            for(int j =0; j< w; j++){
                board[i][j] = dott.charAt(j);
                // System.out.println(board[i][j]); //check each char
            }
        }
            
            
        for(int i =0; i< h; i++){
            for(int j =0; j< w; j++){
                if (i == 0){
                    if(board[i+1][j] == '#'){
                        System.out.println(i+ " " +j);
                    }
                }else if(i == h-1){
                    if(board[i-1][j] == '#'){
                    System.out.println(i+ " " +j);
                    }
                }else{
                    if(board[i-1][j] == '#' && board[i+1][j] == '#'){
                    System.out.println(i+ " " +j);
                    }
                }
            }
        } 
    }
}


ただし、左端のマスの場合は「右のマスが '#' 」であれば、右端のマスの場合は「左のマスが '#' 」であれば隣接する左右のマスが全て '#' であるものとします。
また、上端のマスの場合は「下のマスが '#' 」であれば、下端のマスの場合は「上のマスが '#' 」であれば隣接する上下のマスが全て "#" であるものとします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

マップの判定・縦横

ints = input().split()

first = int(ints[0])
second = int(ints[1])

# print(first)
# print(second)

strs =[]

#so for read we only need to have one loop 
for i in range(first):
    nexts = input()
    strs.append(nexts)
        
# print(strs)
        
# then we loop to fin the target
for row in range(first):
    # print(row)
    for column in range(second):
        # print(strs[row][column])
        
        left_ok = (column == 0) or (strs[row][column - 1] == '#')
        
        right_ok = (column == second - 1) or (strs[row][column + 1] == '#')
        
        up_ok = (row == 0) or (strs[row - 1][column] == '#')
        
        down_ok = (row == first - 1) or (strs[row + 1][column] == '#')
        
        if left_ok and right_ok and up_ok and down_ok:
            print(row, column)



#python ans from paiza
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        flag_row = False
        flag_column = False

        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                flag_row = True

        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                flag_column = True

        if flag_column and flag_row:
            print(y, x)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] lines= sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(lines));
        
        int h = Integer.parseInt(lines[0]);
        int w = Integer.parseInt(lines[1]);
        
        char[][]board = new char[h][w];
        
        for(int i =0; i< h; i++){
            String dott = sc.next();
            for(int j =0; j< w; j++){
                board[i][j] = dott.charAt(j);
                // System.out.println(board[i][j]); //check each char
            }
        }
            
            
            for(int i =0; i< h; i++){
                for(int j =0; j< w; j++){
    
                boolean leftOk = (j == 0) || (board[i][j - 1] == '#');
                
                boolean rightOk = (j == w - 1) || (board[i][j + 1] == '#');
            
                boolean upOk = (i == 0) || (board[i - 1][j] == '#');
                
                boolean downOk = (i == h - 1) || (board[i + 1][j] == '#');
            
        
                if (leftOk && rightOk && upOk && downOk) {
                    System.out.println(i + " " + j);
                }
            }
        } 
    }
}