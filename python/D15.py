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