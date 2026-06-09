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


