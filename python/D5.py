問題　1.

入力例1
hello paiza

出力例1
hello
paiza

#python
#THERE ARE TWO STRING I NEED TO SEPARATE THEM
input_line = input()
# print(input_line)
# print(input_line.split())

for c in input_line.split():
    # print(input_line.split(c), end="")
    print (c)


#java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] strline = line.split(" ");
        // System.out.println(line);

        
        for(String ans : strline){
            System.out.println(ans);
        }

        sc.close()
    }
}


問題　2.
# 2 つの文字列 S, T が入力されます。S, T を改行区切りで出力してください。

#python
long = 2

while long != 0 :
    input_line = input()
    print(input_line)
    
    long-= 1
    

#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int longest = 2;
        
        for(int i = 0; i < longest; i++ ){
            String line = sc.nextLine();
            System.out.println(line);
        }
        
        sc.close();
    }
}



問題　3.

整数 A, B が与えられます。A と B の差 D と積 P を半角スペース区切りで出力してください。
this is means give you a and b 
D should be a-b P should be a*b


#PYTHON
#---------------METHOD 1-------------------
line = input()
# print(line)

a = line.split()
# print(a)

A1 = int(a[0])
B1 = int(a[1])

# print(A1)
# print(B1)


d =  A1-B1
p =  A1*B1
print(d, p)


#--------------METHOD2------------
# ASSUME "10 5 3"
# 1. DIRECT CHANGE THREE NUMBER INTO THREE VARIABLES
str_a, str_b, str_c = line.split()

# 2. THEN TURN THEM INTO INTEGER
a = int(str_a)
b = int(str_b)
c = int(str_c)


#method3
a, b = map(int, input().split())

print(a - b, a * b)



#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        // System.out.println(line);
        
        
        int d = a - b;
        int p = a * b;
        
        System.out.print("" + d +" " + p);
        // or write System.out.println((a - b) + " " + (a * b));

        sc.close();
        
    }
}



問題 4.

変数 N を 0 で初期化する
N に A を足した値を N へ代入する
N に B をかけた値を N へ代入する
N を C で割ったあまりを N へ代入する
N を出力する


Initialize variable N to 0
Assign to N the value of N plus A
Assign to N the value of N multiplied by B
Assign to N the remainder of N divided by C
Output N

#python

# print(input_line)
# print(A)
# print(N)
A, B, C = map(int, input().split())
N = 0

N += A
N *= B
N %= C

print(N)



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line0 = sc.nextInt();
        int line1 = sc.nextInt();
        int line2 = sc.nextInt();

        int n = 0;
        n += line0;
        n *= line1;
        n %= line2;
        
        System.out.println(n);
        
        sc.close();
    }
}



問題 5.
ある電車に a 人が乗っています。駅に到着した時に b 人が降りて新たに c 人が乗車する時、電車に乗っている乗客人数を求めてください。

so basically it means a - b + c


#python
a, b, c = map(int, input().split())
# print(input_line)

ans = a - b + c

print(ans)


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        System.out.println("XXXXXX");
    }
}


問題 6.
文字列Sが与えられます。Sがpaizaと一致する場合はYESを、一致しない場合はNOを出力してください。



#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println(line);
        
        
        if (line.equals("paiza")){
            System.out.print("YES");
        } else {
            System.out.print("NO");
                
        } 
    }
}


#python
input_line = input()


if input_line == "paiza":
    print("YES")
else:
    print("NO")



問題 7.
整数Nが与えられます。Nが 100 以下の場合はYESを、そうではない場合はNOを出力してください。


#python
input_line = int(input())
# check = int(input_line) 
# print(check)

if input_line <= 100:
    print("YES")
else:
    print("NO")



#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        
        if (line <= 100){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
        
        sc.close();
    }
}



問題 8.
整数 A, B, C が与えられます。式 A × B ≦ C が成立している場合はYESを、そうではない場合はNOを出力してください。



#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line0 = sc.nextInt();
        int line1 = sc.nextInt();
        int line2 = sc.nextInt();

        // System.out.println("XXXXXX");
        int ans = line0 * line1;
        
        if (ans <= line2){
            System.out.print("YES");
        } else {
            System.out.print("NO");
        }
        
        sc.close();
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

a, b, c = map(int, input().split())
# print(input_line)

ans = a * b 

if ans <= c:
    print("YES")
else:
    print("NO")



問題 9.
ある占いでは、箱の中に 1~9 までのいずれかの数字が書かれている玉を取り出し、その玉に書かれている数字から運勢を占います。玉に書かれている数字が 7 の時は大吉となります。占いで取り出した玉に書かれている数字が 1 つ与えられます。大吉かどうかを判定してください。

this means the number is from 1 to 9 and if the number == 7 then it should be yes otherwise be no

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

n = int(input())

# if n < 1 and n > 10:
#     exit()

if n >= 1 and n <= 9:
    if n == 7:
        print("Yes")
    else:
        print("No")


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println("XXXXXX");
        if (line < 1 || line > 10){
            return ;
        }
        //  print(n)
        if (line == 7 ){
            System.out.print("Yes");
        }else{
            System.out.print("No");
        }
        
        sc.close();
    }
}


問題 10.
1 ~ N の整数を 1 から順に改行区切りで出力してください。
based on n we need to print 1 to n


# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
input_line = int(input())
# print(input_line)

# ・ 1 ≦ N ≦ 100

for i in range(input_line +1 ):
    if i >= 1 and i <= 100:
        print (i)



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        for (int i = 1; i<= line; i++){
            if(i >= 1 && i <=100){
                // System.out.print(i+"\n");
                System.out.println(i);  //equals
            }
        }
        
        sc.close();
        
    }
}





問題 11.

1 ~ 100 の整数に対して、3 と 5 の両方で割り切れるなら FizzBuzz を、 3 でのみ割り切れるなら Fizz 、5 でのみ割り切れるなら Buzz を改行区切りで出力してください。また、どちらでも割り切れない場合は、その数字を改行区切りで出力してください。

1
2
Fizz
4
Buzz

# so this is basically say this will give you some number and depend whether it can be divide by 3 or 5 
#if both then show fizzbuzz if its 3 then fizz if its 5 then go with buzz

#python

for i in range(1, 101):
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


i = 1
while i <= 100:
    # print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
        
    i += 1



#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        
        for(int i = 1; i<=100; i++){
            // System.out.println(i);
            if(i % 3 ==0 && i % 5 == 0){
                System.out.println("FizzBuzz");
            }else if(i % 3 ==0){
                System.out.println("Fizz");
            }else if(i % 5 ==0){
                System.out.println("Buzz");
            }else{
                System.out.println(i);
            }
        }
    }
}