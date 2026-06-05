「足すか掛けるか Python3編」

2つの整数の組がn個与えられるので、各組の計算結果を足し合わせたものを出力してください。
各組の計算結果は次の値です。
・2つの整数の組を足し合わせたもの
・ただし、2つの整数が同じ値だった場合は、掛け合わせたもの

manys = int(input())
# print(manys)

ans = 0
tem = 0

for i in range(manys):
    nexts = input().split()
    # print("this is next:",nexts)
    a = int(nexts[0])
    b = int(nexts[1])
    # print("1. here a :", a)
    # print("2. here b :", b)
    
    # print("here is tem:", tem)
    # for here we will need to a == b 
    if a == b:
            tem += a * b
            # print("we hit here:",tem)
    else :
            tem += a + b
    #         print("here is tem:",tem)
    # print("-------------")
            
print(tem)


問題問題
string to int 

文字列が入力されるので、その長さを出力してください。

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String [] lines = line.toString().split("");
        // System.out.println(Arrays.toString(lines));
        
        // count =0;
        
        System.out.println(lines.length);
        
        // for (int i = 0; i< lines.length; i++){
            
        // }
        
        
        sc.close();
    }
}