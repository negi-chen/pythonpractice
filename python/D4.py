


# 1.
#想要的輸出格式是 1 1（中間只有空格，沒有中括號和逗號）
#java

public class Main {
    public static void main(String[] args) {
        int[] alist = {1, 1};
        
        for (int i = 0; i < alist.length; i++) {
            System.out.print(alist[i]);
            
            // if this is not the last number add a space 
            if (i < alist.length - 1) {
                System.out.print(" ");
            }
        }
        // final change to next line
        System.out.println(); 
    }
}



# 2.
#python
#WE EXPECT THE OUTPUT IS 6409
        
#METHOD ONE
A = 1231
B = 5178

X = A + B
print(X)

#METHOD TWO (MORE EFFICIENT)
print(1231 + 5178)



# 3.
# 整数 A = 437,326、 B = 9,085 とします。以下の二つの演算の結果を半角スペース区切りで出力してください。

# 1. A を B で割った商
# 2. A を B で割った余り
# A // B is exactly what you need for the first part (Integer Division / Quotient).
# A % B is exactly what you need for the second part (Remainder / Modulo).
# SO THIS IS LIKE WANT A // B  and this in java is A / B
# AND SECOND IS LIKE WANT A % B


#JAVA
public class Main {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        // Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        
        int A = 437326;
        int B = 9085;
        int X = A / B;
        int Y = A % B;

        System.out.println(""+ X +" "+ Y);
        #ABOVE PRINT WE CAN USE ANOTHER METHOD BELOW
        System.out.printf("%d %d\n", A / B, A % B);
    }
}

    # IN JAVA WE CAN ALSO DO BELOW
        var a = 437_326;
        var b = 9_085;

        System.out.println((a / b) + " " + (a % b));

#PYTHON
A = 437326
B = 9085 

X = A // B
Y = A % B

print(X, Y)




# 「代入演算 1 Java編」採点結果
     # 変数 N を 0 で初期化する
     # N に 3,286 を足した値を N へ代入する
     # N に 4,736 をかけた値を N へ代入する
     # N を 12,312 で割った余りを N へ代入する
    
     import java.util.*;

public class Main {
    public static void main(String[] args) {
        // # 変数 N を 0 で初期化する
        // # N に 3,286 を足した値を N へ代入する
        // # N に 4,736 をかけた値を N へ代入する
        // # N を 12,312 で割った余りを N へ代入する
        // # N を出力する

        
        // Scanner sc = new Scanner(System.in);
        // String line = sc.nextLine();
        int N = 0;
        N += 3286;
        N *= 4736;
        N %= 12312;
        
        System.out.println(N);
    }
}