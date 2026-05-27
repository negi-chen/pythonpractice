# Hackerrank
# Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # print(n)
    
    # for n in range(n):
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird") 
        if n >= 6 and n <= 20:
            print("Weird")
        if n > 20 :
            print("Not Weird") 
    elif n % 2 != 0: 
        print("Weird")



#problem 1
# paiza de java and python
「1 つの文字列を出力 」

#1.java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        System.out.println("paiza");
    }
}


#2.python
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
# input_line = input()
print("paiza")




#problem 2
期待する出力
答えの文字列を 1 行で出力してください。

paiza learning

末尾に改行を入れ、余計な文字、空行を含んではいけません。


#1.java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        System.out.println("paiza learning");
    }
}

#basic
import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        System.out.println("813");
    }
}



#THIS IS INT ARRAY
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        int[] alist = {8, 1, 3};
        int length = alist.length;
        for(int i = 0; i< length; i++){
            System.out.println(alist[i]);
        }
    }
}


#THIS IS STRING
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        String alist = "813";
        int length = alist.length();
        for(int i = 0; i< length; i++){
            System.out.println(alist.charAt(i));
        }
        
    }
}


#2.python
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
# input_line = input()
print("paiza learning")



# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
# input_line = input()
# easy method
print(8)
print(1)
print(3)

#method two list
a = [8, 1, 3]
for c in range(len(a)):
    print(a[c])

#method three string
a =  ("813")
for c in range(len(a)):
    print(a[c])


