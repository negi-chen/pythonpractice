

from platform import java_ver


1. warm up
入力される値
入力は以下のフォーマットで与えられます。

s
入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。


theinput = str(input())
# print(theinput)


ans = theinput[0]
# for i in theinput:
#     print()

print(ans)


2.java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println(line);
        String[] ans = line.split("");
        
        List <String> list = new ArrayList<>();
        list.add(ans[0]);
        
        // for (int i = 0; i< line.length();i ++){
        //     list.add(line);
        //     System.out.println(list);
        // }
        // list.split();
        System.out.println(ans[0]);
    }
}




#count number
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String [] change = line.split(" ");
        
        int one = Integer.parseInt(change[0]);
        int two = Integer.parseInt(change[1]);
        // System.out.println(one);
        for (int i = one; i < two+1; i++){
            System.out.println(i);
        }
    }
}


3.文字列を切り取る

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
inputs = input().split()
# print(inputs)

one = int(inputs[0])
two = int(inputs[1])

inputs2 = input()
# print(inputs2)
 
 
for i in range(one-1, two):
    # print(i)
    print(inputs2[i], end ="")
# count = two - one + 2
# print(count) 
# while count > 0:
#     for c in inputs2:
#         print(c)
#     count -=1
    
    # while one < two+2:
        
        
    #     one += 1
        

#or method 2
nums = input().split()
string = input()

print(string[int(nums[0]) - 1 : int(nums[1])])


#or method 3
# 1行目の入力を取得し、スペースで分けて整数に変換
one, two = map(int, input().split())

# 2行目の文字列を取得
inputs2 = input()

# スライスを使って指定された範囲を切り出す
# 1始まりのインデックスを0始まりに合わせるため、開始は one - 1
# 終了は two の直前まで（= two文字目まで）なので、そのまま two を指定
answer = inputs2[one - 1:two]

# 結果を出力
print(answer)



#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String [] change = line.split(" ");
        int c = 0;
        
        String next = sc.nextLine();
        int one = Integer.parseInt(change[0]);
        int two = Integer.parseInt(change[1]);
        // System.out.println(one);
        for (int i = one-1; i < two; i++){
            System.out.print(next.charAt(i));
        }
    }
}

#method 2
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int start = scanner.nextInt();
        int end = scanner.nextInt();
        scanner.nextLine(); // 読み飛ばし
        String string = scanner.nextLine();

        System.out.println(string.substring(start - 1, end));

        scanner.close();
    }
}



#python
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
inputs = input()
print(inputs)
#ord() 把字元轉成數字 char into number
ans = chr(ord(inputs) - 32)

print(ans)


#method 2
inputs = input()

#.upper() turn into larger char
ans = inputs.upper()
print(ans)


# java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char line = sc.next().charAt(0);
        // System.out.println(line);
        ?casue here will become int so we need to turn char back from int 
        char ans = (char)(line -32);

        System.out.println(ans);
    }
}

#method 2
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String inputs = scanner.next();
        System.out.println(inputs.toUpperCase());
        
        scanner.close();
    }
}

#method3
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        char inputs = scanner.next().charAt(0);
        System.out.println(Character.toUpperCase(inputs));
        
        scanner.close();
    }
}



finalll question
入力例1
2 6
this is a pen

出力例1
tHIS Is a pen


inputs = input().split()
# print(inputs)

one = int(inputs[0])
two = int(inputs[1])
 
inputs2 = list(input())
# print(inputs2)
# lists = list(inputs)
 
for i in range(one-1, two):
    # print(inputs2[i])
    inputs2[i] = inputs2[i].upper()
    
# print(inputs2)
# use"".join() to let char turn back to string
ans = "".join(inputs2)
print(ans)
    
    



import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String [] change = line.split(" ");
        int c = 0;
        
        String next = sc.nextLine();
        StringBuilder sb = new StringBuilder(next);
        
        int one = Integer.parseInt(change[0]);
        int two = Integer.parseInt(change[1]);
        // System.out.println(one);
        for (int i = one-1; i < two; i++){
            //first get the biggest char of the position 
            char upper = Character.toUpperCase(sb.charAt(i));
            //then set new to the position 
            sb.setCharAt(i, upper);
            
        }
        
        System.out.println(sb.toString());
    }
}

#methods2
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int start = scanner.nextInt();
        int end = scanner.nextInt();
        scanner.nextLine();
        String string = scanner.nextLine();

        System.out.println(string.substring(0, start - 1) + string.substring(start - 1, end).toUpperCase() + string.substring(end));
    }
}





#question1
入力例1
input

出力例1
i
n
p
u
t


import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String str[] = scan.nextLine().split("");

    for (String p : str) {
        System.out.println(p);
    }
  }
}





#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char target = sc.next().charAt(0);
        sc.nextLine();
        String str = sc.nextLine();
        
        int count = 0;
        // System.out.println(one);
        for (int i = 0; i< str.length(); i++){
            // System.out.print(line.charAt(i));
            if (str.charAt(i) == target){
                count += 1;
            }
        }
        System.out.println(count);
    }
}




#question q
THIS IS SLIDING WIDOWS
入力例1
AA
abdeeAAbAAAbfde

出力例1
3

入力例2
el
scale

出力例2
0


#sliding window
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String target = sc.nextLine();
        String strings = sc.nextLine();
        
        int count = 0;
        int targetL = target.length();
        int stringsL = strings.length();
        
        for (int i = 0; i<= stringsL-targetL; i++){
            //  but this only slice two numbers each
            String tem = strings.substring(i, targetL+i);
            // System.out.println(tem);
            if(tem.equals(target)){
                count ++;
            }
        }
        System.out.println(count);
    }
}



first  =  str(input())
second =  str(input())

firstL = len(first)
secondL = len(second)

count = 0
for i in range(0, secondL-firstL+1):
    tem = second[i: i+firstL]
    if(tem == first):
        count += 1
    
print(count)