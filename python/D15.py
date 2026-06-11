「五目並べ（斜め） Python3編」

one =0
two =0
countone = 0
counttwo = 0

#SO FOR THIS QUESTION WE WILL HAVE TO MAKE THE COUNT AT THE BEGINNING
#THAT IF COUNT IS 25 THEN ONE OF WHICH WILL BE THE WINNER
board = []

for x in range(5):
    key = input()
    # print("each board:" , key)
    board.append(key)
    # CAUSE RIGHTNOW WE HAVE TO CHECK THE ROW SO YES WE HAVE EACH LINE

#1. here is for the right anchor and consistantly add grabe the rounds 
for i in range(5):
    # for row in range(5):
    char = board[i][i]
    # print("first char*", char)
    
    if char == "O" :
        countone += 1
    elif char == "X":
        counttwo += 1
    else:
        None
    
    # print("countone*", countone)
        
#2. here to check second rounds
for i in range(5):
    countdown = 4
    char2 = board[i][countdown-i]
    # print("second char*",char2)
    
    if char2 == "O" :
        one += 1
    elif char2 == "X":
        two += 1
    else:
        None
    # print("one*",one)
        
#here to check the final ans
if countone == 5 or one == 5:
    print("O")
elif counttwo == 5 or two == 5:
    print("X")
else:
    print("D")



#ans from paiza
board = []
result = "D"
direction = [True, False]

for i in range(5):
    board.append(input())

for reverse in direction:
    pivot = ""
    count = 0

    if reverse:
        j = 0
        j_diff = 1
    else:
        j = 4
        j_diff = -1

    for i in range(5):

        stone = board[i][j]

        if pivot == "":
            pivot = stone

        if stone != "." and stone == pivot:
            count += 1

        j = j + j_diff

    if count == 5:
        result = pivot
        break

print(result)



「五目並べ（斜め） Java編」

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // here is all the counter 
        int five = 0;
        int countone = 0;
        int counttwo = 0;
        int one = 0;
        int two = 0;
        // here is all init the string[]
        String change[] = new String[5];
        
        // put each string inside 
        while (five < 5){
            // System.out.println(s);
            change[five] = sc.nextLine();
            five +=1;
        // System.out.println(Arrays.toString(change));
        }
        
        // then loop each round and grabe the numbers
        for (int i = 0; i < 5; i++){
            char each = change[i].charAt(i);
            // System.out.println(each);
            
            if(each == 'O'){
                one +=1;
            }else if (each == 'X'){
                two +=1;
            }else{
                
            }
            // System.out.println(one);
        }
        
        
        
        for (int i = 0; i < 5; i++){
            int countdown = 4;
            char each2 = change[i].charAt(countdown-i);
            // System.out.println(each2);
            
            if(each2 == 'O'){
                countone +=1;
            }else if (each2 == 'X'){
                counttwo +=1;
            }else{
                
            }
        }
        
        if(one == 5 || countone == 5){
            System.out.println("O");
        }else if (two == 5 || counttwo == 5){
            System.out.println("X");
        }else{
            System.out.println("D");
        }
    }
}


入力される値
なし


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
各ユーザーについて順に、ユーザーとユーザーに対応する血液型を半角スペース区切りで出力してください。
最後は改行し、余計な文字、空行を含んではいけません。


Forans ={
    "Kyoko": "B",
    "Rio": "O",
    "Tsubame": "AB",
    "KurodaSensei": "A",
    "NekoSensei": "A"
}

for user, blood in Forans.items(): #this is total two columns
    # print(f"{user} {blood}")
    print(f"{user} {blood}")



import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        HashMap<String, String> forAns = new LinkedHashMap<>();
        
        forAns.put("Kyoko", "B");
        forAns.put("Rio", "O");
        forAns.put("Tsubame", "AB");
        forAns.put("KurodaSensei", "A");
        forAns.put("NekoSensei", "A");
        
        for (Map.Entry<String, String> entry : forAns.entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
        
    }
}


n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
そのあとで連想配列（辞書）をそのまま表示してください。

number = int(input())
# print(number)

maps = {}

for i in range(number):
    a = input().split()
    # print(a[0])
    # print(a[1])
    maps[a[0]] =  a[1]
    # print(maps)

for key, value in maps.items():
    print(key, value)




#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lines = sc.nextInt();
        // System.out.println(lines);
        sc.nextLine();
        HashMap<String, String> maps = new LinkedHashMap<>();
        
        for(int i =0; i< lines; i++){
            String puts[] = sc.nextLine().split(" ");
            // System.out.println(Arrays.toString(puts));
            maps.put(puts[0], puts[1]);
        }
        // System.out.println(maps);
        
        for(Map.Entry<String, String> entry: maps.entrySet()){
            System.out.println(entry.getKey()+ " "+ entry.getValue());
        }
        sc.close();
    }
}




「1人の血液型 Python3編」
1行目でユーザーが1つ与えられます。
n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
その連想配列（辞書）の中で1行目で与えられたユーザー名と、ユーザー名に対応する血液型を表示してください。



target = input()
# print(target)

datas = int(input())
maps = {}

for i in range(datas):
    lines = input().split()
    a = lines[0]
    b = lines[1]
    # print(a)
    maps[a] = b
    # print(maps)
    
for key, value in maps.items():
    # print(i)
    if target == key :
        print(key, maps[key])




#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine();
        int lines = sc.nextInt();
        // System.out.println(lines);
        sc.nextLine();
        HashMap<String, String> maps = new LinkedHashMap<>();
        
        for(int i =0; i< lines; i++){
            String puts[] = sc.nextLine().split(" ");
            // System.out.println(Arrays.toString(puts));
            maps.put(puts[0], puts[1]);
        }
        // System.out.println(maps);

        for(Map.Entry<String, String> entry: maps.entrySet()){
            if(entry.getKey().equals(target)){
            System.out.println(entry.getKey()+ " "+ entry.getValue());
            }
        }
        sc.close();
    }
}





#basic for this we need to have to map and match two datas
次のような占いプログラムを作成してください。

最初に「ユーザー」 U が1つ与えられます。
続いて n 人の「ユーザー」と「ユーザーに対応する血液型」が与えられます。
続いて m 種類の「血液型」と「血液型に対応する占い結果」が与えられます。

与えられたユーザー U に対応する占い結果を表示してください。

入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。

#python
target = input()
# print(target)

datas = int(input())
maps = {}
maps2 = {}

for i in range(datas):
    lines = input().split()
    a = lines[0]
    b = lines[1]
    # print(a)
    maps[a] = b
    # print(maps)
    
datas2 = int(input())
# print(datas2)

for i in range(datas2):
    lines = input().split()
    a = lines[0]
    b = lines[1]
    # print(a)
    maps2[a] = b
    # print(maps2)

for key, value in maps.items():
    # print(i)
    if target == key :
    #remember the value
        final = maps[key]

for key, value in maps2.items():
    # print(i)
    if final == key :
        print(maps2[final])




#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String target = sc.nextLine();
        int lines = sc.nextInt();
        // System.out.println(lines);
        sc.nextLine();
        HashMap<String, String> maps = new LinkedHashMap<>();
        HashMap<String, String> maps2 = new LinkedHashMap<>();
        
        
        for(int i =0; i< lines; i++){
            String puts[] = sc.nextLine().split(" ");
            // System.out.println(Arrays.toString(puts));
            maps.put(puts[0], puts[1]);
        }
        // System.out.println(maps);
        
        int nextLines = sc.nextInt();
        sc.nextLine();
        
        for(int i =0; i< nextLines; i++){
            String puts[] = sc.nextLine().split(" ");
            // System.out.println(Arrays.toString(puts));
            maps2.put(puts[0], puts[1]);
        }

        String ans = new String();
        for(Map.Entry<String, String> entry: maps.entrySet()){
            if(entry.getKey().equals(target)){
            ans = entry.getValue();
            }
        }
        // System.out.println(ans);
        
        for(Map.Entry<String, String> entry: maps2.entrySet()){
            if(entry.getKey().equals(ans)){
            System.out.println(entry.getValue());
            }
        }
        sc.close();
    }
}



#ans from paiza
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, String> bloodTypeMap = new HashMap<String, String>();
        HashMap<String, String> fortuneMap = new HashMap<String, String>();

        // 入力値の処理
        String user = scanner.nextLine();

        int n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i++) {
            String[] bloodType = scanner.nextLine().split(" ");
            bloodTypeMap.put(bloodType[0], bloodType[1]);
        }

        int m = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < m; i++) {
            String[] fortune = scanner.nextLine().split(" ");
            fortuneMap.put(fortune[0], fortune[1]);
        }
        // 入力値の処理ここまで

        String bloodType = bloodTypeMap.get(user);
        String fortune = fortuneMap.get(bloodType);

        System.out.println(fortune);
        scanner.close();
    }
}


#ans from paiza
target = input()

n = int(input())
users = {}
for i in range(n):
    tmp = input().split()

    users[tmp[0]] = tmp[1]

m = int(input())
fortunes = {}
for i in range(m):
    tmp = input().split()

    fortunes[tmp[0]] = tmp[1]

user_blood = None
for user, blood in users.items():
    if user == target:
        user_blood = blood
        break

for blood, fortune in fortunes.items():
    if blood == user_blood:
        print(fortune)
        break





次のような占いプログラムを作成してください。

「ユーザー」と「ユーザーに対応する血液型」、「血液型」と「血液型に対応する占い結果」が与えられます。

それぞれのユーザーに対応する占い結果を表示してください。

入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // String target = sc.nextLine();
        int lines = sc.nextInt();
        sc.nextLine(); 
        
        HashMap<String, String> maps = new LinkedHashMap<>();
        for(int i = 0; i < lines; i++){
            String puts[] = sc.nextLine().split(" ");
            maps.put(puts[0], puts[1]);
        }
        
        int nextLines = sc.nextInt();
        sc.nextLine(); 
        
        HashMap<String, String> maps2 = new LinkedHashMap<>();
        for(int i = 0; i < nextLines; i++){
            String puts[] = sc.nextLine().split(" ");
            maps2.put(puts[0], puts[1]);
        }
        
        HashMap<String, String> combinedMap = new LinkedHashMap<>();
        
        for(Map.Entry<String, String> entry: maps.entrySet()){
            String user = entry.getKey();
            String blood = entry.getValue();
            
            if(maps2.containsKey(blood)){
                String tem = maps2.get(blood);
                combinedMap.put(user, tem);
            }
        }
        
        for(Map.Entry<String, String> entry: combinedMap.entrySet()){
            System.out.println(entry.getKey()+ " "+ entry.getValue());
        }
        
            // System.out.println(combinedMap);
        
        sc.close();
    }
}




# input first
datas = int(input())
maps = {}
maps2 = {}
# print(datas)

for i in range(datas):
    lines = input().split()
    a = lines[0]
    b = lines[1]
    # print(a)
    maps[a] = b
    # print(maps)

# input second
datas2 = int(input())
# print(datas2)

for i in range(datas2):
    lines = input().split()
    a = lines[0]
    b = lines[1]
    # print(a)
    maps2[a] = b
    # print(maps2)

map3 = {}

for key, value in maps.items():
    # print(i)
    #remember the value
    user = key
    blood = value
    # print(user)
    for key, value in maps2.items(): 
        if blood == key:
            # print(value)
            tem2 = value
            # print(value)
            map3[user] = tem2

# print(map3)


for key, value in map3.items():
#     # print(i)
    print(key, value)
    
    
    