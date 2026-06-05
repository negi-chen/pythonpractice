問題1

答えを 1 行で出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。
The question is asking you to find the smallest natural number that is greater than or equal to 10,000 and is perfectly divisible by 13.

# line = int(input())
# print(line)

# so basically i have to find the number above 10000
# numbers >= 10000:
#     numbers // 13
#     if number == 769
#     for 769 * 13 
#     and add 13 will be 10010
    
ans = 10000
ans = 10000 // 13
# print(ans)

ans = ans * 13
# print(ans)

ans = ans + 13
print(ans)

#then i have to divid them with 13


#then the smallest number will be 100010


#ans from paiza
n = 10000

while True:
    if n % 13 == 0:
        break

    n += 1

print(n)



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        // System.out.println();
        
        int target = 10000;
        
        boolean search = true;
        while (search != false){
            if(target % 13 == 0){
                break;
            }else{
                target++;
            }
        }
        System.out.println(target);
    }
}



問題2
パイザ君と霧島京子は最初どちらも数 1 をもっています。パイザ君は自分の番が来ると、自分のもっている数の a 倍を霧島京子の数に足してあげます。霧島京子は自分の番が来ると、自分のもっている数を b で割った余りをパイザ君の数に足してあげます。この手続きをパイザ君の番から始めて、霧島京子の数がnより大きくなるまで繰り返します。

a = 1
b = 1
Both Paiza-kun and Kyoko start with the number 1. They take turns making moves, starting with Paiza-kun.👑 Paiza-kun's turn: Adds ($a \times$ his current number) to Kyoko's number.🌸 Kyoko's turn: Adds (her current number % b) to Paiza-kun's number.The process repeats until Kyoko's number is strictly greater than $n$.Goal: Output the total number of times Paiza-kun performed his turn.


#python
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
limit = int(input())
# print(limit)

twonumb = input().split()
a =int(twonumb[0])
b =int(twonumb[1])

# print(twonumb)
# print(a, b)

p = 1 
k = 1

count = 0

while True:
    # 1. first round is p will *p then add to k  
    k = k +(p*a)
    # 2. second round is k will % b to tem
    tem = k % b
    p += tem
    count += 1
    if k > limit:
        print(count)
        break
    

# print(k)
# print(tem)
# print(p)



#ans from paiza
n = int(input())
[a, b] = input().split()
a, b = int(a), int(b)
paiza = 1
kyoko = 1

times = 0

while True:
    times += 1
    kyoko += paiza * a

    if kyoko > n:
        break

    paiza += kyoko % b

print(times)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int target = sc.nextInt();
        // System.out.println(target);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        int p = 1;
        int k = 1;
        
        int temp = 0;
        int count = 0;
        boolean loop = true;  
        
        while (loop){
            k = k + (p * a);
            // System.out.println(k);
            temp = k % b;
            // System.out.println(temp);
            p += temp;
            // System.out.println(p);
            count ++;
            // System.out.println(count);
            if (k > target){
                System.out.println(count);
                break;
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
        int a = sc.nextInt();
        int b = sc.nextInt();

        int paiza = 1;
        int kyoko = 1;
        int times = 0;

        while (true) {
            times += 1;
            kyoko += paiza * a;

            if (kyoko > n) {
                break;
            }

            paiza += kyoko % b;
        }

        System.out.println(times);
    }
}


問題3

# question's question
M_n = P{n-1} times 2 + P_{n-2}


H = int(input())


P = [0, 1, 1]  
M = [0, 1, 1] 

turn = 1

while True:
    if turn > 2:
        current_P = M[turn - 1] + M[turn - 2]
        P.append(current_P)

        current_M = P[turn - 1] * 2 + P[turn - 2]
        M.append(current_M)
    else:
        current_M = 1

    H -= current_M

    if H <= 0:
        print(turn)
        break

    turn += 1



#python 2
# ここからコードを書き始めてください
paiza = int(input())
# print(paiza)

# paizah2 = 1
# monsterh = 1

# basicstart = 1  #track
# paiza = paiza - 2


# # p3 = m2 + m1 = 2  #i think we can go stright from stage 2
# paizah = monsterh + monsterh

# # m3 = p3*2 + p2
# monsterh = paizah *2 + paizah

# paiza = paiza - monsterh

# basicstart += basicstart

# print(basicstart)



p_prev1 = 1  
p_prev2 = 1  
m_prev1 = 1  
m_prev2 = 1  

turn = 1

while True:
    if turn > 2:
        p_current = m_prev1 + m_prev2
        m_current = p_prev1 * 2 + p_prev2
    else:
        p_current = 1
        m_current = 1

    paiza -= m_current

    if paiza  <= 0:
        print(turn)
        break


    if turn > 1:
        p_prev2 = p_prev1
        p_prev1 = p_current

        m_prev2 = m_prev1
        m_prev1 = m_current

    turn += 1


#abs from paiza
H = int(input())

# N <= 10**12

a = [0, 1, 1]
b = [0, 1, 1]

dmg = 2

i = 2

while dmg < H:
    a[0] = a[1]
    a[1] = a[2]
    b[0] = b[1]
    b[1] = b[2]

    a[2] = b[0] + b[1]
    b[2] = a[0] + 2 * a[1]

    dmg += b[2]

    i += 1

print(i)





#java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // int h = sc.nextInt();
        // System.out.println(h);
        
        // List <Integer> pa = new ArrayList<>(List.of(0, 1, 1));
        // List <Integer> mon = new ArrayList<>(List.of(0, 1, 1));
        
        // System.out.println(pa);
        
        // int round = 2;
        // int count = 2;
        
        // while (round < ){
            
        // }
        
        long h = sc.nextLong(); 
        
        List<Long> pa = new ArrayList<>(List.of(0L, 1L, 1L));
        List<Long> mon = new ArrayList<>(List.of(0L, 1L, 1L));
        
        int round = 1;
        
        while (true) {
            long current_mon_dmg;
            
            if (round > 2) {
                pa.set(0, pa.get(1));
                pa.set(1, pa.get(2));
                mon.set(0, mon.get(1));
                mon.set(1, mon.get(2));
                
                pa.set(2, mon.get(0) + mon.get(1));
                mon.set(2, pa.get(1) * 2 + pa.get(0));
                
                current_mon_dmg = mon.get(2);
            } else {
                current_mon_dmg = 1;
            }

            h -= current_mon_dmg;
            
            if (h <= 0) {
                System.out.println(round);
                break;
            }
            round++;
        }
    }
}




#ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();

        int[] paiza = {0, 1, 1};
        int[] monster = {0, 1, 1};
        int dmg = 2;
        int times = 2;

        while (dmg < h) {
            paiza[0] = paiza[1];
            paiza[1] = paiza[2];
            monster[0] = monster[1];
            monster[1] = monster[2];

            paiza[2] = monster[0] + monster[1];
            monster[2] = paiza[0] + paiza[1] * 2;

            dmg += monster[2];

            times += 1;
        }

        System.out.println(times);
    }
}




問題 ????

出力例1
Hello
World

入力例2
apple orange

出力例2
apple
orange

入力例3
12 345

出力例3
12
345

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // System.out.println(line);
        // int lengths = line.length();
        
        while(sc.hasNext()){
            String line = sc.next();
            System.out.println(line);
        }
        // for (int i = 0; i < lengths; i++){
        //     // System.out.println();
        //     System.out.print(line.charAt(i));
        // }
    }
}

