
問題1
n 人の人に関して、それぞれの人の名前と財産が与えられます。
その後に人名 S が与えられるので （S は最初に与えられた名前のうちのいずれか）、
 S の財産を表す整数を出力してください。



#python


peoples = int(input())
# print("peoples:", peoples)

namebox = []

for i in range(peoples):
    nameandpro = input().split()
    # print(nameandpro)
    namebox.append(nameandpro)

# print(namebox)
    
target = str(input())
# print(target)

for c in namebox:
    # print("datas:" ,c)
    # print("datas:" ,c[0])
    if target == c[0]:
        print(c[1])



#ans from paiza
n = int(input())
zaisan = {}

for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a

S = input()

print(zaisan[S])


# java
from tokenize import group
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int peoples = sc.nextInt();
        String cut = sc.nextLine();
        // System.out.println(peoples);
        List <String> listFor = new ArrayList<>();  
        String input;
        
        while(peoples > 0){
            input = sc.nextLine();
            // System.out.println("*numberandpro: "+input);
            listFor.add(input);
            // System.out.println("*whole: "+listFor);
            peoples --;
        }
        
        String target = sc.nextLine();
        // System.out.println("--target--: "+target);
        
        String[] each;
        
        for (int i = 0; i< listFor.size(); i++){
            // System.out.println("--list--: "+ listFor.get(i));
            each = listFor.get(i).split(" ");
            // System.out.println("--check--: "+ each[0]);
            
            if(target.equals(each[0])){
                System.out.println(each[1]);
            }
            
        }
    }
}



#ans from paiza

import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        HashMap<String, Integer> sa = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = sc.next();
            int a = sc.nextInt();

            sa.put(s, a);
        }

        System.out.println(sa.get(sc.next()));
    }
}


問題2
--入力例1
2
Kirishima
Kyoko
2
Kyoko 1
Kyoko 2
Kyoko

--出力例1
3

--入力例2
3
paiiza
paiza
paiiiza
2
paiiza 2
paiiiza 3
paiza

--出力例2
0


#python


peoples = int(input())
# print("peoples :", peoples)
thismap = {}


for i in range(peoples):
    c = input()
    thismap[c] = 0
    
# print("firststage:", thismap)
    
howmany = int(input())

for i in range(howmany):
    [a, b] = input().split()
    # print([a,b])
    thismap[a] = thismap[a] + int(b) 
    # print([a, b])
    
# print(thismap)

theans = input()
# print(theans)

print(thismap[theans])



#ans from paiza
n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

S = input()

print(dmg[S])



# java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int peoples = sc.nextInt();
        // System.out.println(peoples);
        //need a map and log them
        HashMap <String, Integer> map = new HashMap<>();
        
        for(int i = 0; i< peoples; i++){
            String name = sc.next();
            int none = 0;
            
            map.put(name, none);
        }
        
        // System.out.println(map);
        
        
        int attacts = sc.nextInt();
        
        while(attacts > 0){
            String names = sc.next();
            int attact = sc.nextInt();
            
            map.put(names, map.get(names) + attact);
            
            attacts --;
        }
        
        System.out.println(map.get(sc.next()));
    }
}


#ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        HashMap<String, Integer> pa = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = sc.next();
            
            pa.put(s, 0);
        }

        int m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            String p = sc.next();
            int a = sc.nextInt();
            
            pa.put(p, pa.get(p) + a);
        }

        System.out.println(pa.get(sc.next()));
    }
}



問題3

1 行目には正整数 n が与えられ、 2 行目から (n + 1) 行目には人の名前 s_1, ..., s_n が改行区切りで与えられます。 (n + 2) 行目には正整数 m が与えられ、 (n + 3) 行目から (n + m + 2) 行目には人の名前 p_i （s_1, ..., s_n のいずれか） とその人が受けたダメージ a_i が "p_i a_i" という半角スペース区切りのフォーマットで m 行与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。


期待する出力
それぞれの人が受けたダメージを、人の名前のアルファベットの辞書順に n 行出力してください（出力するのはダメージだけです）。
末尾に改行を入れ、余計な文字、空行を含んではいけません。



#wrong ans for reserve the values
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
peoples = int(input())
# print("peoples :", peoples)
thismap = {}


for i in range(peoples):
    c = input()
    thismap[c] = 0
    
# print("firststage:", thismap)
    
howmany = int(input())

for i in range(howmany):
    [a, b] = input().split()
    # print([a,b])
    thismap[a] = thismap[a] + int(b) 
    # print([a, b])
    
#then this is basically want we reverse 
sort = sorted(thismap.values(),reverse=True)
# print(thismap)
# print(sort)

for i in sort:
    print(i)


##this time beacuse question want us to print the alphabeta order of name]
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
peoples = int(input())
# print("peoples :", peoples)
thismap = {}


for i in range(peoples):
    c = input()
    thismap[c] = 0
    
# print("firststage:", thismap)
    
howmany = int(input())

for i in range(howmany):
    [a, b] = input().split()
    # print([a,b])
    thismap[a] = thismap[a] + int(b) 
    # print([a, b])
    
#then 人の名前のアルファベットの辞書順に出力してください
sort = sorted(thismap.keys())
# print(thismap)
# print(sort)

for i in sort:
    print(thismap[i])



#ans from paiza
n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

names = list(dmg.keys())
names.sort()

for name in names:
    print(dmg[name])


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int peoples = sc.nextInt();
        // System.out.println(peoples);
        //need a map and log them
        HashMap <String, Integer> map = new HashMap<>();
        
        for(int i = 0; i< peoples; i++){
            String name = sc.next();
            int none = 0;
            
            map.put(name, none);
        }
        
        // System.out.println("1:"+map);
        
        
        int attacts = sc.nextInt();
        
        while(attacts > 0){
            String names = sc.next();
            int attact = sc.nextInt();
            
            map.put(names, map.get(names) + attact);
            
            attacts --;
        }
        // System.out.print("2:"+map);
        
        List <String> nameList = new ArrayList<>(map.keySet());
        
        Collections.sort(nameList);
        
        // System.out.println(nameList);
        
        for (int i = 0; i< nameList.size();i ++ ){
            String out = nameList.get(i);
            System.out.println(map.get(out));
        }
    }
}



#ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        HashMap<String, Integer> pa = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String s = sc.next();

            pa.put(s, 0);
        }

        int m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            String p = sc.next();
            int a = sc.nextInt();

            pa.put(p, pa.get(p) + a);
        }

        ArrayList<String> keyList = new ArrayList<>(pa.keySet());
        Collections.sort(keyList);

        for (String i : keyList) {
            System.out.println(pa.get(i));
        }
    }
}


問題4

期待する出力
A グループの i_c 番目の人が C グループの k_c 番目の人に仕事を頼むとしたとき （1 ≤ c ≤ p） 、各 i_c, k_c をそれぞれ半角スペース区切りで、 i_c が小さい順に p 行出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。

from a group search to b group and then to c group
final link a to c 


groups = input().split()
# print(groups)

putapeoples = {}
putcpeoples = {}

agroup = int(groups[0])
bgroup = int(groups[1])
cgroup = int(groups[2])

# print(agroup,bgroup,cgroup)
for i in range(agroup):
    [a, b] = input().split()
    putapeoples[a] = b

# print(putapeoples)

for i in range(bgroup):
    [b2, c] = input().split()
    putcpeoples[b2] = c


for i in range(1, agroup+1):
    a_first = str(i)
    # print(i)
    b_trace = putapeoples[a_first]
    c_trace = putcpeoples[b_trace]
    
    print(a_first,c_trace)
# print(putcpeoples)
    


#ans from paiza
[p, q, r] = [int(i) for i in input().split()]
AB = {}
BC = {}

for _ in range(p):
    [i, j] = [int(n) for n in input().split()]
    AB[i] = j

for _ in range(q):
    [j, k] = [int(n) for n in input().split()]
    BC[j] = k

AC = {}

for i in range(1, p + 1):
    AC[i] = BC[AB[i]]

for i, k in AC.items():
    print(i, k)



#JAVA
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        Map <String, String> forAB = new HashMap<>();
        Map <String, String> forBC = new HashMap<>();
        
        for (int i = 0; i< a ; i++){
            //i need to put a and b in the map
            String a1 = sc.next();
            String b1 = sc.next();
            // System.out.println(a1); 
            // System.out.println(b1); 
            forAB.put(a1, b1);
            // System.out.println(forAB); 
            
        }
        
        
        for (int i = 0; i< b ; i++){
            //i need to put a and b in the map
            String b2 = sc.next();
            String c2 = sc.next();
            // System.out.println(b2); 
            // System.out.println(c2); 
            forBC.put(b2, c2);
            // System.out.println(forBC); 
        }
        
        
        for (int x =1; x<=a; x++){
            //right here is the value of a cause a will from 01234 order
            String afirst = String.valueOf(x);
            // System.out.println(afirst); 
            
            String btrace = forAB.get(afirst);
            // System.out.println(btrace); 
            String ctrace = forBC.get(btrace);
            // System.out.println(ctrace);
            
            System.out.println(afirst +" "+ ctrace);
        }
        sc.close();
    }
}

..wrong
        // String line = sc.nextLine().split();
        // String[] split = line.split(" ");
        
        // System.out.println(Arrays.toString(split));
        // for (int i = 0; i< 3; i++){
        //  System.out.println(Arrays.toString(split.charAt(i)));
        //     System.out.println(split.charAt(i));  
        // }




# ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        int q = sc.nextInt();
        int r = sc.nextInt();

        HashMap<Integer, Integer> ab = new HashMap<>();
        HashMap<Integer, Integer> bc = new HashMap<>();

        for (int x = 0; x < p; x++) {
            Integer i = sc.nextInt();
            Integer j = sc.nextInt();

            ab.put(i, j);
        }

        for (int x = 0; x < q; x++) {
            Integer j = sc.nextInt();
            Integer k = sc.nextInt();

            bc.put(j, k);
        }

        ArrayList<Integer> keyList = new ArrayList<>(ab.keySet());
        Collections.sort(keyList);

        for (Integer x : keyList) {
            System.out.println(x + " " + bc.get(ab.get(x)));
        }
    }
}