
問題1


入力例1
1
a
2
paiza
kyoko

出力例1
YES
NO

入力例2
2
c
d
2
cat
dog

出力例2
YES
NO
NO
YES


for this weird question, clearly we cant use set......
so below is wrong answer.....

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
rangeone = int(input())
# print(rangeone) debugger

targetlist = []

for i in range(rangeone):
    target =  input()   #this is setup as map() we change mind cause here only one char
    targetlist.append(target)
# print(targetlist) debugger
    
    
rangetwo = int(input())
# print(rangetwo)  debugger


for c in range(rangetwo):
    wordset = set(input()) #changehere
    # print(wordset) debugger
    # to be continute here we are going to loop the aimtocheck and whether the target inside?
    # print(f"{wordset} : {target}") debugger 
    # okay because this is the loop it will take each set of word inside like a whole character
    
    for t in targetlist:
        if t in wordset:     #change here
            print("YES")
        else:
            print("NO")
    
    
    # aimtocheck = list(map(str, input()))  # so here will be the bester choice to set a map?
    # print(aimtocheck)
    # for v in aimtocheck:
        # print(v)
        


# correct one
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
rangeone = int(input())
# print(rangeone) debugger

targetlist = []

for i in range(rangeone):
    target =  input()   #this is setup as map() we change mind cause here only one char
    targetlist.append(target)
# print(targetlist) debugger
    
    
rangetwo = int(input())
# print(rangetwo)  debugger


#clearly we have to make both a list
wordsets = []

for c in range(rangetwo):
    wordset = input()
    # print(wordset)
    wordsets.append(wordset)
# print(wordsets)
    # to be continute here we are going to loop the aimtocheck and whether the target inside?
    # print(f"{wordset} : {target}") debugger 
    # okay because this is the loop it will take each set of word inside like a whole character

for t in targetlist:
    # print(t)
    for w in wordsets:
        # print(w)
        if t in w:     
            print("YES")
        else:
            print("NO")
    
    # aimtocheck = list(map(str, input()))  # so here will be the bester choice to set a map?
    # print(aimtocheck)
    # for v in aimtocheck:
        # print(v)
        


#answer from paiza
m = int(input())
c = [""] * m

for i in range(m):
    c[i] = input()

n = int(input())
S = [""] * n

for i in range(n):
    S[i] = input()

for i in range(m):
    for j in range(n):
        if c[i] in S[j]:
            print("YES")
        else:
            print("NO")


# java

from socketserver import ThreadingMixIn
import java.util.*;


public class Main {
    public static void main(String[] args) {
        // two int two list 
        // good habit is to prepare the tools first
        Scanner sc = new Scanner(System.in);
        int number1 = sc.nextInt();
        // System.out.println(number1);
        List <String> li1 = new ArrayList<>();
        List <String> li2 = new ArrayList<>();
        
        // first add
        for (int i = 0; i< number1; i++){
            String li11 = sc.next();
            li1.add(li11);
        }
        // System.out.println(li1);
        
        int number2 = sc.nextInt();
        // System.out.println(number2);
        
        // second add
        for (int i = 0; i< number2; i++){
            String li22 = sc.next();
            li2.add(li22);
        }
        // System.out.println(li2);
        
        
        //use first char to check each word
        for (String i : li1){
            // System.out.println("whether each char:"+i);
            for (int j = 0; j< li2.size(); j++){
                // System.out.println("and each word: "+li2.get(j));
                //MIGHT NEED TO LOOP li2??
                // System.out.println(i + " : HERE :"+ li2.get(j));
                if (li2.get(j).contains(i)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
    }
}



#answer of paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        
        String[] c = new String[m];

        for (int i = 0; i < m; i++) {
            c[i] = sc.next();
        }

        int n = sc.nextInt();
        String[] s = new String[n];

        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (s[j].contains(c[i])) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }
}



問題2
期待する出力
入力された通りの順番で、各参加者の得点をN回、改行区切りで出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。



入力例2
4 5 2
1 3 4 4 5
2 2 2 2 2
1 2 3 4 5
1 1 1 1 1

出力例2
0
5
1
0

FOUR PEOPLES FIVE GRADES ADN THEN FINAL IS THAT WHO GETS THE SAME NUMBER AS IT
COUNT THE NUMBER OF THEM



??wrong answer

#PYTHON

# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

inputs = list(input().split())
# print(inputs)

#might nees to extract each number
#1
people = int(inputs[0])

#2
scores = int(inputs[1])

#3
targets = int(inputs[2])

# print(people)
# print(scores)  basically dont care about this
# print(targets)

#three list
#three loops

# whether we hit or not
count = 0

inputpeoples =[]
for i in range(people):
    # print(i)
    eachlist = input().split()
    # print(eachlist)
    inputpeoples.append(eachlist)
# print(inputpeoples)
        

for a, b in inputpeoples:
        # print("a *",a,"b *", b)
    # print("===every colums===:", inputpeoples)
    x = int(a)
    y = int(b)
    # print("targets",targets)
    if x == targets or y == targets: 
        count += 1
    #     print("check x:",x)
    #     print("count:", count)
    # # if y == targets:
    #     # count += 1
    #     print("check y:",y)
    #     print("count:", count)
    
# print("final:", count)
    print(count)
# placeagain = inputpeoples.split()
# print(placeagain)

# for x in range(scores): #here is loop the each columns
    #inside this i wanna loops
    

#     for scores in inputpeoples:
#         print(scores)
    # print(inputpeoples[])
    # for c in inputpeoples:
    # print(inputpeoples(x))
                # print(c)
        # print("this is :", i)

#     if targets in c:
#         count += 1
        
#     print(count)


#-------------correct one
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

inputs = list(input().split())
# print(inputs)

#might nees to extract each number
#1
people = int(inputs[0])

#2
scores = int(inputs[1])

#3
targets = int(inputs[2])

# print(people)
# print(scores)  basically dont care about this
# print(targets)

#three list
#three loops

# whether we hit or not

inputpeoples =[]
for i in range(people):
    # print(i)
    eachlist = input().split()
    # print(eachlist)
    inputpeoples.append(eachlist)
# print(inputpeoples)
        

    
# print("===every colums===:", inputpeoples)
for row in inputpeoples:
    # print("each rows:", row)
    count = 0
    for scores in row:
        # print(scores)
        if int (scores) == targets:
            count += 1
    print(count)
    # print("targets",targets)
    # print("final:", count)



# ans of paiza
N, M, K = map(int, input().split())

for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)



#to debug
N, M, K = map(int, input().split())

print(N, M, K)

for i in range(N):
    print("this is how many people:" ,i)
    a = [int(j) for j in input().split()]
    ans = 0
    print("each peoples scores :" ,a)
    for j in range(M):
        print("scores:",j)
        if a[j] == K:
            ans += 1
    print(ans)



#java
。?? so for this question we don't need any datas that need to be store
everytime i saw the data and i stores that's all

import java.util.*;


public class Main {
    public static void main(String[] args) {
        // basic three int two list and a count two int 
        // System.out.println();
        Scanner sc = new Scanner(System.in);
        int people= sc.nextInt();
        int scores= sc.nextInt();
        int target= sc.nextInt();
        
        List <Integer> list = new ArrayList<>();
        int [] list1 = new int [scores];
        
        // loop people rows
        for (int i = 0; i< people; i++){
            // list = sc.nextInt();
            // System.out.println(list);
            // list.split();
            int count = 0;
            for (int j  = 0; j< scores; j++){
                int score = sc.nextInt();
                // System.out.print(score + "\n");
                if (score == target){
                    count += 1;
                } 
            }
            System.out.println(count);
        }
        
    }
}

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        
        for (int i = 0; i < n; i++) {
            int[] a = new int[m];

            for (int j = 0; j < m; j++) {
                a[j] = sc.nextInt();
            }

            int ans = 0;

            for (int j = 0; j < m; j++) {
                if (a[j] == k) {
                    ans += 1;
                }
            }
            
            System.out.println(ans);
        }
    }
}


問題3
n 個の数 a_1, … , a_n が与えられます。与えられた数を小さい順に改行区切りで出力してください。


# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

#ok reverse
howmany = int(input())
# print("how many:", howmany)

reversesint = [] 

for i in range(howmany):
    ints = int(input())
    # print(ints)
    reversesint.append(ints)
    
reversesint.sort()
# print(reversesint)

for c in reversesint:
    print(c)
    

#face the int and string's different and this will cause outcome different


#ans of paiza

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort()

for i in range(n):
    print(a[i])


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int howMany = sc.nextInt();
        List <Integer> list = new ArrayList <>();
        // System.out.println(howMany);
        // int[] change = new int[howMany]; //no need
        
        for(int c = 0; c < howMany; c++){
            String just =  sc.next();
            // System.out.println(just);
            list.add(Integer.parseInt(just));
        }
        // System.out.println(list);
        
        Collections.sort(list);
        
        for (int i : list){
            System.out.println(i);
        }
        
        // for (String x :list){
        //     change.add(Integer.parseInt(x));
        // }
        
        // lsit.sort();
    }
}


#ans of paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Arrays.sort(a);

        for (int i = 0; i < n; i++) {
            System.out.println(a[i]);
        }
    }
}





問題4
期待する出力
a_1, ..., a_n を大きい順に並べ替え、改行区切りで n 行、順に出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。

#java
import java.util.*;


public class Main {
  public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int howMany = sc.nextInt();
        List <Integer> list = new ArrayList <>();
        // System.out.println(howMany);
        // int[] change = new int[howMany]; //no need
        
        for(int c = 0; c < howMany; c++){
            String just =  sc.next();
            // System.out.println(just);
            list.add(Integer.parseInt(just));
        }
        // System.out.println(list);
        
        Collections.sort(list, Collections.reverseOrder());
        
        for (int i : list){
            System.out.println(i);
        }
  }
        
}




#ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        Integer[] a = new Integer[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Arrays.sort(a, Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            System.out.println(a[i]);
        }
    }
}



#python
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort()

x = n-1
# print(x)
while n> 0:
    # for x in range(n):
    print(a[x])
    n = n - 1
    x = x -1



#anwer of paiza

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort(reverse = True)

for i in range(n):
    print(a[i])





問題5
期待する出力
ペアを偉い順に並べ替え、改行区切りで n 行、順に出力してください。出力の各行は入力と同じく、 "a_i b_i" のように、りんごの個数とバナナの数が、この順に、半角スペースで区切られているものとします。
末尾に改行を入れ、余計な文字、空行を含んではいけません。

# ==========================================================

# 【Python3】標準入力の書き方に困ったらこちら！
# 「入力される値」の取得方法一覧（Python）

# https://paiza.jp/pages/works/cheatsheet/stdin_python

# ==========================================================

# ここからコードを書き始めてください

depend = int(input())
# print(depend)

code = []

for i in range(depend):
    lists = list(map(int, input().split()))
    code.append(lists)
    # print(code)


code.sort(reverse = True)

for j in code:
    print(*j)
    

#ans from paiza
n = int(input())
ab = [None] * n

for i in range(n):
    [a, b] = input().split()
    a = int(a)
    b = int(b)
    ab[i] = [a, b]

ab.sort(reverse=True)

for i in range(n):
    [a, b] = ab[i]
    print(a, b)


#java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String[] ab = new String[n];

        for (int i = 0; i < n; i++) {
            String a = sc.next();
            String b = sc.next();

            if (a.length() == 1) {
                a = "0" + a;
            }
            
            if (b.length() == 1) {
                b = "0" + b;
            }

            ab[i] = a + b;
        }

        Arrays.sort(ab, Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            System.out.println(Integer.parseInt(ab[i].substring(0,2)) + " " + Integer.parseInt(ab[i].substring(2,4)));
        }
    }
}


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int howMany = sc.nextInt();
        sc.nextLine(); 
        
        List<int[]> list = new ArrayList<>();
        
        // System.out.println(howMany);
        
        for (int c = 0; c < howMany; c++) { 
            String just = sc.nextLine();
            
            String[] parts = just.split(" "); 
            
            int a = Integer.parseInt(parts[0]); 
            int b = Integer.parseInt(parts[1]); 
            
            list.add(new int[]{a, b});
        }
        
 
        list.sort((o1, o2) -> {
            if (o2[0] != o1[0]) {
                return Integer.compare(o2[0], o1[0]);
            }
            return Integer.compare(o2[1], o1[1]);
        });
        

        for (int[] pair : list) {
            System.out.println(pair[0] + " " + pair[1]);
        }
    }
}



問題6
N 人の人々がおり、それぞれの人は金と銀を何キログラムか持っています。今は金の方が銀よりも価値が高いですが、ある日金と銀の価値が逆転して、人々の財産の多さは次のように決定されるようになりました。

1. 持っている銀が多い方が財産が多い。
2. 持っている銀が同じなら、持っている金が多い方が財産が多い。

それぞれの人が持っている金と銀のキログラム数が与えられるので、この規則にしたがって、財産を多い順に並び替えて出力してください。


