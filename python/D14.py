#the アルファベットの範囲の文字の出力 Python3編
alph = input()
# print(alph)

first = alph[0]
final = alph[len(alph)-1]
#we got the alph we want then loop 
# print(first, final)

#change alph into number
first = ord(first)
final = ord(final)

for i in range(first, final+1):
    print(chr(i))



#the 「アルファベットの範囲の文字の出力 Java編」

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        // System.out.println();
        // String alph[] = line.split("");　⁇no need??
        // System.out.println(Arrays.toString(alph)); 
        int len = line.length()-1; 
        char finals = line.charAt(len);
        char first = line.charAt(0);
        
        for (char i = first; i< finals+1; i++ ){
            System.out.println(i);
        }
        
    }
}





# the アルファベットの順番 Java編

import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int len = line.length()-1; 
        char finals = line.charAt(len);
        char first = line.charAt(0);
        
        // System.out.println(finals +" "+ first);
        
        // here turn the char into number clearly this called Widening Casting
        int finals1 = finals;
        int first1 = first;
        
        // System.out.println(finals1 +" "+ first1);
        
        if(finals1 < first1){
            System.out.println("false");
        }else{
            System.out.println("true");
        }
        
    }
}



# the 「アルファベットの順番 Python3編」

alph = input()
# print(alph)

first = alph[0]
final = alph[len(alph)-1]
#we got the alph we want then loop 
# print(first, final)

#change alph into number then compare them
first = ord(first)
final = ord(final)
# print(first, final)

if first < final:
    print("true")
else:
    print("false")




#the 「アルファベット探し Python3編」


#three inputs
first = input()
mid = input()
final = input()
#we got the alph we want then loop 
# print(first, mid ,final)

#change alph into number then compare them
first = ord(first)
mid = ord(mid)
final = ord(final)
# print(first, mid, final)

count = 0

for i in range(first, mid+1):
    # print(i)
    if final == i:
        count+=1
    else:
        None
        
if count >= 1:
    print("true")
else:
    print("false")
        


#アルファベット探し Java編
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        // int len = line.length()-1; 
        String one = sc.nextLine();
        String two = sc.nextLine();
        String three = sc.nextLine();
        char first = one.charAt(0);
        char second = two.charAt(0);
        char threes = three.charAt(0);
        
        // System.out.println(one +""+ two +""+ three);
        
        // here turn the char into number clearly this called Widening Casting
        int f1 = first;
        int s2 = second;
        int t3 = threes;
        
        // System.out.println(finals1 +" "+ first1);
        boolean check = false;
        
        for(int i =f1; i<=s2; i++){
            if (t3 ==i){
                check = true;
                // #id check then we have find the goal otherwise it will cover the ans
                break;
            }
        }
        
        if(check == true){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
        
    }
}



#ans from paiza
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char x = sc.next().charAt(0);
        char y = sc.next().charAt(0);
        char c = sc.next().charAt(0);
        System.out.println(x <= c && c <= y);
    }
}




入力される値
入力は以下のフォーマットで与えられます。

s


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
勝者の記号を1行で表示してください。
勝者がいない場合は、引き分けとして、"D"を表示してください。



key = input()
# print(key)

countone = 0
counttwo = 0

for i in key:
    # print(i)
    if i == "O" :
        countone += 1
    elif i == "X":
        counttwo += 1
    else:
        None

        
#check 
if countone == 5:
    print("O")
elif counttwo == 5:
    print("X")
else:
    print("D")




#ans from paiza
board = input()
result = "D"

pivot = board[0]
count = 0
for stone in board:
    if stone != "." and stone == pivot:
        count += 1
    else:
        break

if count == 5:
    result = pivot

print(result)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        // System.out.println(s);
        
        // >HERE iwas trying to split and make sure every char is o or x  
        String change [] = s.split("");
        // System.out.println(Arrays.toString(change));
        
        for(String i :change){
            //  System.out.println(i);
        }
        
        // >here i just use the most quick way to complete it
        
        if(s.equals("OOOOO")){
            System.out.println("O");
        }else if (s.equals("XXXXX")){
            System.out.println("X");
        }else{
            System.out.println("D");
        }
    }
}






五目並べ(横) Python3編


one =0
two =0

for x in range(5):
    key = input()
    # print(key)
    # oh right if we want everytime to renew the counter 
    # we might have to put inside the loop
    countone = 0
    counttwo = 0
    for i in key:
        # print(i)
        if i == "O" :
            countone += 1
        elif i == "X":
            counttwo += 1
        else:
            None
    
    # print(countone)
    # print(counttwo)    
    
    #check 
    if countone == 5:
        one +=1
    elif counttwo == 5:
        two +=1
    else:
        None
        

if one == 1:
    print("O")
elif two == 1:
    print("X")
else:
    print("D")


#ans from paiza
result = "D"

for i in range(5):
    board = input()

    pivot = board[0]
    count = 0
    for stone in board:
        if stone != "." and stone == pivot:
            count += 1
        else:
            break

    if count == 5:
        result = pivot


print(result)




五目並べ(横) Java編
入力される値
入力は以下のフォーマットで与えられます。

s_1
s_2
s_3
s_4
s_5


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。
期待する出力
勝者の記号を1行で表示してください。
勝者がいない場合は、引き分けとして、"D"を表示してください。



import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 5;
        int one = 0;
        int two = 0;
        while (count > 0){
            String s = sc.nextLine();
            // System.out.println(s);
            
            // >here i just use the most quick way to complete it
            if(s.equals("OOOOO")){
                one +=1;
            }else if (s.equals("XXXXX")){
                two +=1;
            }else{
               
            }
            count -=1;
        }
        
        if(one == 1){
            System.out.println("O");
        }else if (two == 1){
            System.out.println("X");
        }else{
            System.out.println("D");
        }
    }
}



#ans from paiza
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String result = "D";

        for (int i = 0; i < 5; i++) {
            String input = scanner.next();
            
            if (input.equals("OOOOO")) {
                result = "O";
            } else if (input.equals("XXXXX")) {
                result = "X";
            }
        } 

        System.out.println(result);
        scanner.close();
    }
}



五目並べ（縦） Python3編     縦（直向）
#PYTHON  Nested Loop

one =0
two =0

#SO FOR THIS QUESTION WE WILL HAVE TO MAKE THE COUNT AT THE BEGINNING
#THAT IF COUNT IS 25 THEN ONE OF WHICH WILL BE THE WINNER
board = []

for x in range(5):
    key = input()
    # print("each boar:" ,key)
    board.append(key)
    # CAUSE RIGHTNOW WE HAVE TO CHECK THE ROW SO YES WE HAVE EACH LINE
    
for column in range(5):
    counttwo = 0
    countone = 0
    for row in range(5):
        char = board[row][column]
        # print(char)

        if char == "O" :
            countone += 1
        elif char == "X":
            counttwo += 1
        else:
            None
    
    # print(countone)
    # print(counttwo)    
        #check 
    if countone == 5:
        one +=1
    elif counttwo == 5:
        two +=1
    else:
        None
        

if one == 1:
    print("O")
elif two == 1:
    print("X")
else:
    print("D")


        

#ans from paiza

board = []
result = "D"

for i in range(5):
    board.append(input())

for i in range(5):
    pivot = ""
    count = 0

    for j in range(5):
        stone = board[j][i]

        if pivot == "":
            pivot = stone

        if stone != "." and stone == pivot:
            count += 1
        else:
            break

    if count == 5:
        result = pivot
        break


print(result)




五目並べ（縦） Java編      縦（直向）
#JAVA   loads system printout is for debug
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        String change[] = new String[5];
        boolean ones = true;
        boolean twos = true;
        
        while (count < 5){
            change[count] = sc.nextLine();
        count +=1;
        }
        // System.out.println(Arrays.toString(change));
            
        for (int i = 0; i< 5; i++){
            int one = 0;
            int two = 0;
            // System.out.println(t1);
            for(int y =0; y< 5; y++){
                char target = change[y].charAt(i);
                // System.out.println(target);
                if(target == 'O'){
                    one ++;
                }else if (target == 'X'){
                    two ++;
                }else{
                    break;
                }
            }
        //  System.out.println("--how many--");
        //  System.out.println("maru:"+one);
        //  System.out.println("batsu:"+two);
        if(one == 5){
            ones = false;
            // System.out.println("ones:"+ones);
        }else if (two == 5){
            twos = false;
        }else{
        }
        // System.out.println("==========");
        } 
    
        if(ones == false){
            System.out.println("O");
        }else if (twos == false){
            System.out.println("X");
        }else{
            System.out.println("D");
        }    
    }
}






