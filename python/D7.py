
問題 1


# 0 ~ 9 の数字が 4 つ並んだ文字列 S が与えられます。
# 左から 1 番目の数と 4 番目の数を足し合わせたものを a とし、 2 番目の数と 3 番目の数を足し合わせたものを b とします。

# 文字列としての a の末尾に文字列としての b を結合したものを出力してください。


java

# method one 
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        // System.out.println(line);
        
        int lengthOf = line.length();
        // System.out.println("how long: " + lengthOf);
        int a = 0;
        int b = 0;
        
        // System.out.println("the a : " + a);
        int first = 0;
        int last = 0;
        int second = 0;
        int third = 0;
        
        first = Character.getNumericValue(line.charAt(0));
        last = Character.getNumericValue(line.charAt(3));
        second = Character.getNumericValue(line.charAt(1));
        third = Character.getNumericValue(line.charAt(2));
        
        a = first + last;
        // System.out.println("a: " + a);
        b = second + third;
        // System.out.println("b: " + b);
        System.out.println(a+ ""+ b);

        
        /*
        // StringBuilder sb2 = new StringBuilder();
        // sb2.append(line.charAt(1) + line.charAt(2));
        // System.out.println("sb2: " + sb2.append(line.charAt(1) + line.charAt(2)));
        // System.out.println("sb2: " + sb2);
        
        here is wrong methods
        for(int i = 0; i< lengthOf; i++){
            System.out.println(line.charAt(i));
            // i need to add element one and final element
            sb.append(line.charAt(i));
            sb2.append(line.charAt(0));
            // and then add element two with three
        }
        
        */
    }
}


# method 2
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] sArray = s.split("");

        String a = Integer.toString(Integer.parseInt(sArray[0]) + Integer.parseInt(sArray[3]));
        String b = Integer.toString(Integer.parseInt(sArray[1]) + Integer.parseInt(sArray[2]));
        
        System.out.println(a + b);
    }
}


#python

#method1
line = input()
# print(line)

# this = int(line)  //this is wrong one
# print(this)

a = int(line[0]) + int(line[3])
b = int(line[1]) + int(line[2])


# 1
print(a, end="")
print(b)
# 2
print(f"{a}{b}")


#method2
S = input()

a = int(S[0]) + int(S[3])
b = int(S[1]) + int(S[2])

print(str(a) + str(b))



問題2

#method1
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // do for this question we should use string perhaps
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println("check input number:" + line);
        int leng = line.length();
        StringBuilder sb = new StringBuilder();
        // System.out.println("check leng:" + leng);
            
        
        if (leng == 3) {  //do nothing
            System.out.println(line);
            return;
        }
        
        if (leng == 2){
            // no ? (one add one)
            sb.append("0");
        }else {
            sb.append("0");
            sb.append("0");
        }
        
        for (int i = 0; i < leng ; i++ ){
            // System.out.print(line.charAt(i));
            sb.append(line.charAt(i));
        }
        System.out.println(sb);
    }
        
        // so here we will need to check whether it have three
        
        // yes return
        
        // no? 
        
            // how many left (two add one)
        
}

# method2

    Scanner sc = new Scanner(System.in);
    String line = sc.nextLine();
    int num = Integer.parseInt(line);
    System.out.printf("%03d", num);


# python

N = input()

while len(N) < 3:
    N = "0" + N

print(N)


#method2
input_line = input()
# print(input_line)

while len(input_line) < 3:
    # input_line += "0" (wrong) this will let 0 add behind
    # ill need to add 0 in front
    input_line = "0" + input_line
    
    
print(input_line)


# method3
line = input()
num = int(line)

print(f"{num:03d}")




# 「数字の文字列操作（時刻1） Python3編」
問題3
# python
input_line = input()
# print(input_line)

hour, minute = map(str, input_line.split(":"))

for i in hour:
    if i == "0":
    # print("hour ls",hour.lstrip(i))
        hour = hour.lstrip(i)
    
for x in minute:
    if x == "0":
    # print(x)
        minute = minute.lstrip(x)
        
if hour =="":
    hour = "0"
    
if minute =="":
    minute = "0"


print(hour)
print(minute)


# method2
S = input()
h = int(S[:2])
m = int(S[3:])

print(h)
print(m)


# java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println(line);
        
        int h = Integer.parseInt(line.substring(0,2));
        int m = Integer.parseInt(line.substring(3));
        
        System.out.println(h);
        System.out.println(m);
    }
}





問題4
# 与えられた時刻の 30 分後の時刻を "XX:XX" の形式で出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# python
#method1
input_line = input()
# print(input_line)


# so base on the clock number we will have to add 30 min
h = int(input_line[:2])
m = int(input_line[3:])

# print(h)
# print(m)

m += 30
# print("new m :", m)


if m >= 60 :
    h += 1
    tem = m - 60 
    m = 0  # yeah if min already over 60 thenit should be 1 
    m += tem

# print("after *",h)
# print("after *",m)

print(f"{h:02d}:{m:02d}")


# python
#method2
S = input()
h = int(S[:2])
m = int(S[3:])

if m + 30 >= 60:
    h = str(h + 1)
    m = str(m + 30 - 60)
else:
    h = str(h)
    m = str(m + 30)

if len(h) == 1:
    h = "0" + h
if len(m) == 1:
    m = "0" + m

print(h + ":" + m)




# java
# method1
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println(line);
        
        int h = Integer.parseInt(line.substring(0,2));
        int m = Integer.parseInt(line.substring(3));
        
        
        // System.out.println(h);
        // System.out.println(m);
        
        m += 30;
        // System.out.println(m);
        int tem = 0;
        
        
        if (m >= 60){
            h += 1;
            tem = m - 60;
            m = 0;
            m += tem;
            
        }
        // System.out.println(h);
        // System.out.println(m);
        System.out.printf("%02d:%02d", h, m);
    }
}


# method2
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        
        int h = Integer.parseInt(s.substring(0, 2));
        int m = Integer.parseInt(s.substring(3, 5));
        
        if (m + 30 >= 60) {
            h = h + 1;
            m = m + 30 - 60; 
        } else {
            h = h;
            m = m + 30; 
        }

        String newH = Integer.toString(h);
        String newM = Integer.toString(m); 

        if (newH.length() == 1) {
            newH = "0" + newH;
        }
        
        if (newM.length() == 1) {
            newM = "0" + newM;
        }

        System.out.println(newH + ":" + newM);
    }
}



問題5
# 期待する出力
# 入力された通りの順番で、各週の工事が終わる時刻を N 行出力してください。時刻の表記は入力と同じフォーマットに従うものとし、 24 時以降は翌日の時刻を記し、 00:00 から 23:59 までの間に収まるように、また、時や分を表す数字が1桁の場合には十の位を 0 で埋めてください。たとえば 24 時は 00:00、 27 時は 03:00 となります。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。


# python
# method1

input_line = int(input())
# print(input_line)

# then next input
while input_line > 0:
    firsttime = str(input())
    # print(firsttime)
    # deal with first data first
    h = int(firsttime[:2])
    m = int(firsttime[3:6])
    
    # print(h)
    # print(m)
    
    # through time
    t1 = int(firsttime[6:8])
    t2 = int(firsttime[8:])
    
    
    # print(t1)
    # print(t2)
    
    h += t1
    m += t2
    # print("new m :", m)
    
    
    if m >= 60 :
        h += 1
        tem = m - 60 
        m = 0  # yeah if min already over 60 thenit should be 1 
        m += tem
    
    # print("see1:" , h)
    # print("see2:" , m)
    
    if h > 24:   
        te = h
        h = te - 24  
        
        
    if h == 24:
        h = 0
        
        
    print(f"{h:02d}:{m:02d}")
    
    input_line -= 1



# python
# method2

input_line = int(input())

while input_line > 0:
    firsttime = input()
    
    start_time, t1_str, t2_str = firsttime.split()
    
    h_str, m_str = start_time.split(":")
    
    h = int(h_str)
    m = int(m_str)
    t1 = int(t1_str)
    t2 = int(t2_str)
    in
    h += t1
    m += t2
    
    if m >= 60:
        h += 1
        m -= 60  
        
    h = h % 24
        
    print(f"{h:02d}:{m:02d}")
    
    input_line -= 1


#java 
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int lengths = Integer.parseInt(sc.nextLine());
        // System.out.println(lengths);
        
        while (lengths > 0){
            String time = sc.nextLine();
            
            
            String[] parts = time.split(" ");
            String startTime = parts[0]; // "12:30"
            String t1Str = parts[1];     // "2"
            String t2Str = parts[2];     // "15"
            
            String[] timeParts = startTime.split(":");
            String hStr = timeParts[0]; // "12"
            String mStr = timeParts[1]; // "30"
            
            int h1 = Integer.parseInt(hStr);
            int m = Integer.parseInt(mStr);
            int t1 = Integer.parseInt(t1Str);
            int t2 = Integer.parseInt(t2Str);
            
            h1 += t1;
            m += t2;
            
            if (m >= 60){
                h1+= 1;
                m-=60;
            }
            
            h1 = h1 % 24;
            
            System.out.printf("%02d:%02d\n", h1, m);
            
            
            lengths --;
        }
    }
}




# 問題6
# 期待する出力
# 与えられた整数の中に3の倍数がいくつあるかを出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
input_line = int(input())
# print(input_line)

ans = input().split()
# print(ans)

counter = 0

for i in ans:
    # print(i)
    numb = int(i)
    # print(numb)
    if numb % 3 == 0:
        counter += 1
            
print(counter)



#method2
n = int(input())
a = input().split()

ans = 0

for i in range(n):
    if int(a[i]) % 3 == 0:
        ans += 1

print(ans)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        int count = 0;
        
        for (int i = 0; i < line; i++ ){
            int nextOne = sc.nextInt();
            // System.out.println(nextOne);
            if (nextOne % 3 == 0){
                count += 1;
            }
        }
        System.out.println(count);
    }
}



問題7
# 期待する出力
# a_1, ..., a_n の中に 7 がひとつでも含まれていた場合には "YES" を、そうでない場合には "NO" を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# python

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
input_line = int(input())
# print(input_line)

check = bool(True)

for i in range(input_line):
    number = int(input())
    if number == 7:
        check = False
        
if check == False:
    print("YES")
else:
    print("NO")


#JAVA

import java.util.*;


public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);
        int line = sc.nextInt();
        // System.out.println(line);
        
        boolean memo = true;
        
        int check = 0;
        for (int i = 0; i < line; i++){
            check = sc.nextInt();
            // System.out.println(check);
            if (check == 7){
                memo = false;
            }
        }
        
        if (memo == false){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}


問題8

# 期待する出力
# 財産が k 円である人の番号を出力してください。ただし、そのような人が複数いる場合には、そうした人々の中で最も小さい番号を出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

# first how many datas
datas = int(input())
# print(datas)

peoples = []

# then how many people?
for i in range(datas):
    people = int(input())
    # print(people)
    peoples.append(people)
# print(peoples)


pro = int(input())

count = 0
for i in peoples:
    count += 1 #this represent the number of peoples that are not the same as pro 
    if i == pro:  #if we found someone whos n == pro then this means we dont need to count 
        break
print(count)



#method2
n = int(input())

a = [0] * n

for i in range(n):
    a[i] = input()

k = input()

for i in range(n):
    if a[i] == k:
        print(i + 1)
        break



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int firstN = sc.nextInt();
        // System.out.println("firstN:" + firstN);
        int i = 0;
        
        int [] peoples = new int[firstN]; 
        while (i < firstN){
            int people = sc.nextInt();
            peoples[i] = people;
            // System.out.println(i);
            i++;
        }
        // System.out.println(Arrays.toString(peoples));
            
        int finals = sc.nextInt();
        // System.out.println(finals);
        
        int count = 0;
        for (int x = 0; x < firstN; x++){
            count += 1;
            if (peoples[x] == finals){
            // System.out.println("here count:" + count);
                // System.out.println("here count:" + x);
                break;
            }
        }
        
        System.out.println(count);
    }
}


問題9