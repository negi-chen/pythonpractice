期待する出力
n 個の組を、「整数」の値で昇順に並べ変え、「文字列」を1行ずつ出力してください。


#java 
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int loop = sc.nextInt();
        // System.out.println(loop);
        sc.nextLine();
        // so we might need to reverse the position of string 
        // use string[][] two dimen array
        // List <String> list = new ArrayList
        String[][] forLoop = new String[loop][];
        for (int i =0; i < loop; i++){
            String each = sc.nextLine();
            // System.out.println(each);
            forLoop[i] = each.split(" ");
            // System.out.println(forLoop);
            // System.out.println(Arrays.toString(forLoop[i]));
        }
        
        Arrays.sort(forLoop, (a,b)-> {
            int num1 = Integer.parseInt(a[1]);
            int num2 = Integer.parseInt(b[1]);
            // System.out.println(num1 +" and "+ num2);
            return num1 - num2;  //THIS IS FOR RESERVE?????
        });
        
        for (String[] row : forLoop){
            // System.out.println(Arrays.toString(forLoop[row]));
            // System.out.println(Arrays.toString(row));
            System.out.println(row[0]);
        }
    }
}


#the answer of paiza
import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int times = scanner.nextInt();
        scanner.nextLine();  // 1行読み飛ばし

        HashMap<Integer, String> hashMap = new HashMap<Integer, String>();
        int index[] = new int[times];
        for (int i = 0; i < times; i++) {
            String input[] = scanner.nextLine().split(" ");
            hashMap.put(Integer.parseInt(input[1]), input[0]);
            index[i] = Integer.parseInt(input[1]);
        }

        Arrays.sort(index);

        for (int i: index) {
            System.out.println(hashMap.get(i));
        }

        scanner.close();
    }
}


#python
first = int(input())
# print(first)

#pythons hash map is
maps = {}

for i in range(first):
    strings = input().split()
    # print(strings)
    # print(strings[2]) #here is aph
    # print(strings[7]) #here is number
    #turn number from string into int
    target = int(strings[1])
    # print(target)
    #then key pair match
    maps[target] = strings[0]
    
    #then we go for sorted
sorteds = sorted(maps)
# print(sorteds)

for k in sorteds:
    print(maps[k])



#ans for paiza
num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])




入力される値
なし

HND, NRT, KIX, NGO, NGO
を要素に持つ配列（リスト）をプログラムで定義し、使用すること。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
配列（リスト）の要素に重複があればtrueを、重複がなかったらfalseを出力する。
最後は改行し、余計な文字、空行を含んではいけません。


import java.util.*;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String[] line = {"HND", "NRT", "KIX", "NGO", "NGO"};
        // System.out.println(Arrays.toString(line));
        
        Set <String> map = new HashSet<>(Arrays.asList(line));
        
        int originalLen = line.length;
        // System.out.println(originalLen);
        
        int newLen = map.size();
        // System.out.println(newLen);
        
        if (originalLen != newLen){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
    }
}



# ans from paiza
class Main {
    public static void main(String[] args) {
        String array[] = {"HND", "NRT", "KIX", "NGO", "NGO"};
        Boolean result = false;
        
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                if (i != j && array[i].equals(array[j])) {
                    result = true;
                    break;
                }
            }

            if (result) {
                break;
            }
        }

        System.out.println(result);
    }
}



#python s code

line = ["HND", "NRT", "KIX", "NGO", "NGO"]
# print(line)

originalLen = len(line)
# print(originalLen)

mapset = set(line)
newlen = len(mapset)

if newlen != originalLen:
    print("true")
else:
    print("false")


#ans from python
array = ["HND", "NRT", "KIX", "NGO", "NGO"]
duplicate = False

for i in range(len(array)):
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            duplicate = True

if duplicate:
    print("true")
else:
    print("false")




入力される値
なし

"HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"
を要素に持つ配列（リスト）をプログラムで定義し、使用すること。
ただし、2つ以上同じ要素が出現するのは、1種類の文字列についてだけです。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
同じ要素の数をカウントして、その数を出力してください。
最後は改行し、余計な文字、空行を含んではいけません。



#the  final
import java.util.*;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String[] line = {"HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"};
        // System.out.println(Arrays.toString(line));
        int originalLen = line.length;
        
        HashMap <String, Integer> map = new HashMap<>();
        // System.out.println(map);
        for(String i : line){
            if (map.containsKey(i)){
                map.put(i, map.get(i)+1);
            }else{
                map.put(i, 1);
            }
        }
        
        for(String key: map.keySet()){
            if(map.get(key) > 1){
                System.out.println(map.get(key));
            }
        }
    }
}


#ans from paiza

import java.util.HashMap;
import java.util.Map.Entry;

class Main {
    public static void main(String[] args) {
        String array[] = {"HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"};
        HashMap<String, Integer> count = new HashMap<String, Integer>();
        
        for (String pattern: array) {
            if (count.get(pattern) != null) {
                count.put(pattern, count.get(pattern) + 1);
            } else {
                count.put(pattern, 1);
            }
        }

        for (Entry <String, Integer> element: count.entrySet()) {
            if (element.getValue() != 1) {
                System.out.println(element.getValue());
            }
        }
    }
}



#python
lists = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]

length =len(lists)

# print(lists)
# print(length)
maps ={}

add = 1

for i in lists:
    # print(i)
    if i in maps:
        maps[i] += 1
    else:
        maps[i] = add
    
    
check = set(maps)
for i in check:
    if(maps[i] >1):
        print(maps[i])


#ans from paiza  
        
array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
count = {}

for pattern in array:
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1

for (key, value) in count.items():
    if value != 1:
        print(value)



文字と整数の組のソート2 Python3編（paizaランク C 相当）
期待する出力
文字とまとめた数値の組を各行で出力してください。
文字と数値は半角スペースで区切ってください。

入力例1
7
A 1
D 6
C 2
G 4
B 70
A 10
B 5

出力例1
B 75
A 11
D 6
G 4
C 2


numbers = int(input())
# print(numbers)

maps = {}

for i in range(numbers):
    lists = input().split()
    # print(lists)
    #split the number inside the values
    key  =lists[0]
    value =int(lists[1])
    if key in maps:
        maps[key] = maps[key] + value
    else:
        maps[key] = value
# print(maps)



ans = sorted(maps.items(), key=lambda x: x[1],reverse= True)
# print(ans)

for key, value in ans:
    print(key, value)



#ans from paiza
num = int(input())
inputs = {}
result = {}

for i in range(num):
    tmp = input().split()

    exist = False
    for (key, value) in inputs.items():
        if key == tmp[0]:
            exist = True

    if exist:
        inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])
    else:
        inputs[tmp[0]] = int(tmp[1])

# ソート用にkeyとvalueを反転させた辞書を作る
for (key, value) in inputs.items():
    result[value] = key

result = sorted(result.items(), reverse=True)

for i in result:
    print(i[1] + " " + str(i[0]))



#java

import java.util.*;


public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int numbers = sc.nextInt();
        // System.out.println(numbers);
        sc.nextLine();
        
        HashMap <String, Integer> map = new HashMap<>();
        
        for (int i = 0; i< numbers; i++){
            String key = sc.next();
            int value = sc.nextInt();
            if (map.containsKey(key)){
                map.put(key, map.get(key) + value);
            } else{
                map.put(key, value);
            }
        }
        // System.out.println(map);
    
        map.entrySet().stream().sorted((a, b) -> b.getValue().compareTo(a.getValue())).forEach(entry-> System.out.println(entry.getKey()+ " " + entry.getValue()));
        
    }
}



#ans in paiza
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    Map<Character, Integer> map = new HashMap<>();
    
    for (int i=0; i<n; i++) {
      char c = sc.next().charAt(0);
      int v = sc.nextInt();
      if (map.containsKey(c))
        map.put(c, map.get(c) + v);
      else
        map.put(c, v);
    }

    List<Integer> ll = new ArrayList<>(map.values());
    Collections.sort(ll);
    Collections.reverse(ll);
    
    for (int v : ll)
      for (Character c : map.keySet())
        if (map.get(c) == v)
          System.out.println(c + " " + v);
  }
}