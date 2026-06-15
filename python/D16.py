
**「盤面の情報取得 Python3編」**

**「盤面の情報取得 Java編」**
 下記の問題をプログラミングしてみよう！
行数 H , 列数 W の盤面があり、各マスには文字が 1 つだけ書かれています。盤面と N 個の y , x 座標 が与えられるので、与えられた座標の文字を順に出力してください。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


#all inputs
inputs = input().split()
# print(inputs)

row = int(inputs[0])
columns = int(inputs[1])

#then come with the numbers of coordinate
coordinate = int(inputs[2])
print(row, columns, coordinate)

board =[]

for i in range(row):
    String = input()
    board.append(String)
    # print(board)
  
  
for i in range(coordinate):
    corone = input().split()
    print(corone)
    x= int(corone[0])
    y= int(corone[1])
    # print(x)
    # print(y)
    
    print(board[x][y])


    

#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] inputs = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(inputs));
        int first = 0;
        int second = 0;
        int coordinate = 0; 
        
        first = Integer.parseInt(inputs[0]);
        second = Integer.parseInt(inputs[1]);
        coordinate = Integer.parseInt(inputs[2]);
        
        String[] board = new String[first];
        
        for (int i = 0; i< first;i++){
            String input = sc.nextLine();
            board[i] = input;
        }
        
        // split() the int inorder to catch out the positions board 
        for (int i = 0; i< coordinate; i++){
            String input2 [] = sc.nextLine().split(" ");
            
            int x = Integer.parseInt(input2[0]);
            int y = Integer.parseInt(input2[1]);
            
            System.out.println(board[x].charAt(y));
        }
    }
}


#ans from paiza
H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
    y, x = map(int, input().split())
    print(S[y][x])



「盤面の情報変更 Java編」
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] inputs = sc.nextLine().split(" ");
        // System.out.println(Arrays.toString(inputs));
        int first = 0;
        int second = 0;
        int coordinate = 0; 
        
        first = Integer.parseInt(inputs[0]);
        second = Integer.parseInt(inputs[1]);
        coordinate = Integer.parseInt(inputs[2]);
        
        char[][] board = new char[first][second];
        
        for (int i = 0; i< first;i++){
            String input = sc.next();
            // System.out.println("first round:"+input);
            for(int j = 0; j< second;j ++){
                // so first it will round [0][0] then [0][1] then[0][2]
                 board[i][j] = input.charAt(j); //will put right char first 
                //  System.out.println("second round:"+input.charAt(j));
            }
        }
        
        // split() the int inorder to catch out the positions board 
        for (int i = 0; i< coordinate; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            // System.out.println(x);
            // System.out.println(y);
            // System.out.println("here s "+board[x][y]);
            board[x][y] = '#';
        }
        
        // System.out.println(board);
        for (int i =0; i< first; i++){
            System.out.println(board[i]);
        }
    }
}




#python
inputs = input().split()
# print(inputs)

row = int(inputs[0])
columns = int(inputs[1])

#then come with the numbers of coordinate
coordinate = int(inputs[2])
# print(row, columns, coordinate)

board =[]

for i in range(row):
    #need to turn here into list then we can change target
    String = list(input())
    board.append(String)
    # print(board)
  
  
for i in range(coordinate):
    corone = input().split()
    # print(corone)
    x= int(corone[0])
    y= int(corone[1])
    # print(x)
    # print(y)
    board[x][y] = "#"
    
for row in board:
    print("".join(row))




#ans from paiza
h, w, n = map(int, input().split())
s = [list(input()) for _ in range(h)]

for _ in range(n):
    y, x = map(int, input().split())
    s[y][x] = "#"

for y in range(h):
    print("".join(s[y]))
