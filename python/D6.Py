#day5 practice!!

1.
#文字列 s が与えられるので s をそのまま出力してください。

整数 n が与えられるので、 n 回、改行区切りで paiza と出力してください。


#java
from doctest import OutputChecker
from tarfile import data_filter
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        for(int i = 0; i< line; i++){
            // String lines = sc.nextLine();
            System.out.println("paiza");
        }
        
    }
}


#python
input_line = int(input())

for c in range(input_line):
    print("paiza")




2.
#整数 n と n 個の整数 a_1, ..., a_n が改行区切りで与えられるので、 a_1, ..., a_n を与えられた順に、改行区切りで出力してください。


#JAVA
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        for(int i = 0; i < line; i++){
            int next = sc.nextInt();
            System.out.println(next);
        }
    }
}

#PYTHON
#METHOD1
input_line = int(input())
# print(input_line)

for c in range(input_line):
    nextline = int(input())
    print(nextline)



#METHOD 2
n = int(input())

for i in range(n):
    a = input()
    print(a)




3.
# a_1, ..., a_n の中で最も大きい数を出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。

#java
#method1
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        // ill need to initilate the number Array
        int [] theBox = new int[line]; 
        
        for(int i = 0; i < line ; i++){
            int next = sc.nextInt();
            // System.out.println(next);
            theBox[i] = next;
        }
        // System.out.println(Arrays.toString(theBox));
        System.out.println(Arrays.stream(theBox).max().getAsInt());
        sc.close();
    }
}

#method2
int max = theBox[0];
for (int i = 1; i < theBox.length; i++) {
    if (theBox[i] > max) {
        max = theBox[i];
    }
}
// then max is the biggest number



#method3
Arrays.sort(theBox);
int max = theBox[theBox.length - 1];
// this time max biggest number，and theBox already been sorted


#python
input_line = int(input())

# print(input_line)

temnumber = []

for i in range(input_line):
    nexint = int(input())
    # print(nexint)
    temnumber.append(nexint)
    # print(temnumber)
    
print(max(temnumber))




#整数 n が与えられるので、n 回、半角スペース区切りで paiza と出力してください。
#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        String c = ("paiza");
        // System.out.println(c);

        # wrong method
        # for(int i = 1; i < line;i++){
        #     System.out.print(c + " ");
        #     // System.out.print(" ");
        #     if(i==line-1){
        #         System.out.print(c );
        #     }
                
        for(int i = 0; i < line;i++){
            // System.out.print(" ");

            // 2. use if - else 「最後のループ」と「通常のループ」が完全に分離され、繰り返し実行されるのを防いでください。
            if(i==line-1){
                System.out.print(c );
            }else{
                System.out.print(c + " ");
            }
        }
    }
}

#method3
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String ans = "paiza";

        for (int i = 0; i < n - 1; i++) {
            ans += " paiza";
        }
        
        System.out.println(ans);
    }
}


#python

# ここからコードを書き始めてください
input_line = int(input())
# print(input_line)
this = str("paiza") 

# print(this)
# print("paiza" *input_line)
for i in range(input_line-1):
    this += (" paiza")
print(this)



# 1 行目には整数 n が与えられ、2 行目には半角スペース区切りの n 個の数 a_1, ..., a_n が 1 行で与えられます。

#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        int i = 0;
        
        while (i < line){
            int next = sc.nextInt();
            System.out.println(next);
            i++;
        }
    }
}


#python
# ここからコードを書き始めてください
input_line = int(input())
# print(input_line)
nextone = input().split()
# print(nextone)

for i in range(input_line):
    new = int(nextone[i])
    print(new)




毎年 5 月 1 日に、自分が運営している会社の社員一覧表を作成しています。表は年度ごとに更新され、社員の名前と年齢が載っています。
ところで、会社のメンバーは昨年度から全く変わらず、社員の誕生日は全員 7 月 7 日だったので、前年度の一覧表の年齢欄をそれぞれ +1 するだけで今年度の表が作れることにパイザ君は気づきました。
so this is something that want us to base on the number to have next number of data
and in the data we have to take out the second index and add 1 to the date then print OutputChecker


#python


#method1
for i in range(input_line):
    s1 = input().split()
    # print(s1)
    # print(s1[0])
    name = s1[0]
    number = int(s1[1])
    # print(s1[1])
    number += 1
    print(name, number)


#method2
N = int(input())

for _ in range(N):
    s_a = input().split()
    print(s_a[0], int(s_a[1]) + 1)




#JAVA
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);

        for(int i = 0; i< line;i ++){
            // StringBuilder sb = new StringBuilder(sc.nextline);
            String name = sc.next();
            // System.out.println(name);
            int number = sc.nextInt();
            // System.out.println(number);
            number += 1;
            
            System.out.println(name + " " + number);
            
        }
    }
}





#整数 n と、 n 個の整数 a_1, ..., a_n が改行区切りで与えられるので、各 a_i (1 ≤ i ≤ n) の文字列としての長さを改行区切りで出力してください。
# 各 a_i (1 ≤ i ≤ n) の文字列としての長さを改行区切りで出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。
#THIS IS THAT WANT US TO PRINT THE LONG OF THE FOLLOWING NUMBERS

#python

input_line = int(input())
# print(input_line)

for i in range(input_line):
    #method1
    # nextline = str(input())
    
    #method2
    nextline = input()
    # print(nextline)
    print(len(nextline))


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        for(int i = 0; i < line; i++){
            int check = sc.nextInt();
            // System.out.println(check);
            String turn = Integer.toString(check);
            // System.out.println(turn);
            System.out.println(turn.length());
        }
    }
}


# 文字 a と文字列 S が与えられるので、 S に a が含まれているかどうか判定し、含まれている場合には “YES” を、そうでない場合には “NO” を出力してください。
# 期待する出力
# S に a が含まれている場合には “YES” を、そうでない場合には “NO” を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

#python 
wrong method
#SO BASICALLY THIS IS MEANS THAT IF INPUT_LINE HAVE NEWINT THEN IT COULD BE YES ELSE NO

input_line = input()
# print(input_line)

newint = input()
# print(newint)
# print(newint.split())


if_true = True;

for x in newint:
    # print(x)
    if x == input_line:
        # print("[Y]")
        if_true
    else:
        if_true = False
        # print("[N]")
        
if if_true == True:
    print("YES")
elif if_true == False:
    print("NO")


#method2
#SO BASICALLY THIS IS MEANS THAT IF INPUT_LINE HAVE NEWINT THEN IT COULD BE YES ELSE NO

input_line = input()
# print(input_line)

newint = input()
# if_true = True;

counting = 0

for x in newint:
    # print(x)
    if x == input_line:
        if_true = True
        counting = 1
        # print("[Y]")
    else:
        if_true = False
        # print("[N]")
        
    # print(if_true)
        
# print(counting)

if counting == 1:
    print("YES")
else: 
    print("NO")


#method 3
a = input()
S = input()

if a in S:
    print("YES")
else:
    print("NO")

#java


#method one
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println(line);
        StringBuilder nextline = new StringBuilder (sc.nextLine());
        // System.out.println(nextline);
        
        boolean memory = false;
        
            char line2 = line.charAt(0);  
        
        for(int i = 0; i < nextline.length(); i++){
            char letter = nextline.charAt(i);
            
            // System.out.println(nextline.charAt(i));
            if (nextline.charAt(i) == line2){
                memory = true;
            }
        }
            
        if (memory == true){
            System.out.print("YES");
        }else{
            System.out.print("NO");
        }
    }
}


#method two
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String s = sc.next();
        
        if (s.contains(a)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}