数列 A についての情報が与えられるので、 1 ~ N の各 i について、和 S_i = A_1 + ... + A_i を求めてください。



number = int(input())
# print(inputs)

rightnow = input().split()
# print(rightnow)
forinput = []

ans = 0

for i in rightnow:
    # print(i)
    forinput.append(int(i))
    
# print(forinput)
    
for y in forinput:
    ans += y
    print(ans)
    
# print("here is x", x)



#ans from paiza
n = int(input())
numbers = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += numbers[i]
    print(sum)


#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        // System.out.println(num);
        int [] array = new int[num];
        int ans = 0; 
        List <Integer> current = new ArrayList<>();
        
        
        for (int i = 0; i < num; i++){
            array[i] = Integer.parseInt(sc.next());
        }
        
        // System.out.println(Arrays.toString(array));
    
        for (int i:array){
            ans += i;
            System.out.println(ans);
        }
    
    }
}



区間和の計算
数列 A とクエリの数について情報が与えられるので、各クエリに答えてください。

・ クエリ
整数 l , u が与えられるので、A_l から A_u までの総和 S_i を出力してください。


#might be the wrong answer
first = int(input())
# print(inputs)
forinput = []
forinput = input().split()
# print(forinput)
second = int(input())
# print(second)
condition = []
for i in range(second):
    line = input().split()
    line = list(line)
    condition.append(line)

# print(condition)

for c in condition:
    l = int(c[0])
    y = int(c[1])
    ans = 0
    # print("===here===")
    for x in range(l, y+1):
        # print("each *" ,x)
        # print("each *", forinput[x])
        ans += int(forinput[x])
    print(ans)


#above will cause runtime error

#ans from paiza
N = int(input())
numbers = list(map(int, input().split()))
n = int(input())

sums = [0]
for i in range(N):
    sums.append(sums[-1] + numbers[i])
    # print(sums)

for _ in range(n):
    l_i, u_i = map(int, input().split())
    print(sums[u_i + 1] - sums[l_i])



#java
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = Integer.parseInt(scanner.nextLine().trim());

        String[] parts = scanner.nextLine().trim().split(" ");
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(parts[i]);
        }

        int n = Integer.parseInt(scanner.nextLine().trim());

        long[] sums = new long[N + 1];
        sums[0] = 0;
        for (int i = 0; i < N; i++) {
            sums[i + 1] = sums[i] + numbers[i];
        }

        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < n; q++) {
            String[] lu = scanner.nextLine().trim().split(" ");
            int l = Integer.parseInt(lu[0]);
            int u = Integer.parseInt(lu[1]);
            sb.append(sums[u + 1] - sums[l]).append("\n");
        }

        System.out.print(sb);
    }
}



「最短の区間 Python3編」
N, target = map(int, input().split())
numbers = list(map(int, input().split()))

# print(N, target, numbers)

left = 0
sums = 0
minlen = N + 1

for right in range(N):
    sums += numbers[right]
    # print("==check right==", right)
    
    while sums >= target:
        currentlen = right - left + 1
        if currentlen < minlen:
            minlen = currentlen
        sums -= numbers[left]
        left += 1
        
        # print("second " , sums)

if minlen == N + 1:
    print(-1)
else:
    print(minlen)
    



import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] firstLine = scanner.nextLine().trim().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int target = Integer.parseInt(firstLine[1]);

        String[] parts = scanner.nextLine().trim().split(" ");
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(parts[i]);
        }

        int left = 0;
        long sum = 0;
        int minlen = N + 1;

        for (int right = 0; right < N; right++) {
            sum += numbers[right];

            while (sum >= target) {
                int currentlen = right - left + 1;
                if (currentlen < minlen) {
                    minlen = currentlen;
                }
                sum -= numbers[left];
                left++;
            }
        }

        if (minlen == N + 1) {
            System.out.println(-1);
        } else {
            System.out.println(minlen);
        }
    }
}


#ANS FROM PAIZA
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0]
for i in range(n):
    sums.append(sums[-1] + numbers[i])

count = float("inf")
start = 0
end = 0
while True:
    if end >= n:
        break
    if sums[end + 1] - sums[start] >= m:
        if end - start + 1 < count:
            count = end - start + 1
        start += 1
    else:
        end += 1

if count == float("inf"):
    count = -1
print(count)



最長の区間

#PYTHON
入力例1
1 10
11

出力例1
0

入力例2
10 27
16 9 2 6 18 3 1 3 6 8

出力例2
5


N, target = map(int, input().split())
numbers = list(map(int, input().split()))

# print(N, target, numbers)

left = 0
sums = 0
maxlen = 0 #pretent original is the smallest

for right in range(N):
    sums += numbers[right]
    # print("==check right==", right)
    
    #here hits our target
    while sums > target:
        sums -= numbers[left]
        left += 1
    
    currentlen = right - left + 1
        # print(currentlen)
    if currentlen > maxlen:
        maxlen = currentlen
        

print(maxlen)




#java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] firstLine = scanner.nextLine().trim().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int target = Integer.parseInt(firstLine[1]);

        String[] parts = scanner.nextLine().trim().split(" ");
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(parts[i]);
        }

        int left = 0;
        long sum = 0;
        int maxlen = 0;

        for (int right = 0; right < N; right++) {
            sum += numbers[right];
            
            // if sum biger then we will have to call this function to make it be on the condition of sum <= target
            while (sum > target) {
                sum -= numbers[left];
                left++;
            }
            int currentlen = right - left + 1;
            if (currentlen > maxlen) {
                maxlen = currentlen;
            }
        }
        System.out.println(maxlen);
    }
}


#ans from paiza
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0]
for i in range(n):
    sums.append(sums[-1] + numbers[i])

count = 0
start = 0
end = 0
while True:
    if end >= n:
        break
    if sums[end + 1] - sums[start] <= m:
        if end - start + 1 > count:
            count = end - start + 1
        end += 1
    else:
        start += 1

print(count)






「区間への足し算 Python3編」
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# print(N, M, numbers)

number = []

condition = []
for i in range(M):
    line = input().split()
    line = list(line)
    condition.append(line)
    
# print(condition)

sums = [0] * (N + 1)

for query in condition:
    l = int(query[0]) 
    u = int(query[1])
    a = int(query[2])
    
    sums[l-1] += a
    sums[u] -= a
        
current_diff = 0
for i in range(N):
    current_diff += sums[i]
    numbers[i] += current_diff
    
for x in numbers:
    print(x)



#ans from paiza

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
add = [0] * (n + 1)

for _ in range(m):
    l_i, u_i, a_i = map(int, input().split())
    add[l_i - 1] += a_i
    add[u_i] -= a_i

for i in range(n):
    print(numbers[i] + add[i])
    add[i + 1] += add[i]




import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        long[] diff = new long[N + 1];

        for (int i = 0; i < M; i++) {
            int l = sc.nextInt();
            int u = sc.nextInt();
            int a = sc.nextInt();

            diff[l - 1] += a;
            if (u < N) {
                diff[u] -= a;
            }
        }

        long currentDiff = 0;
        for (int i = 0; i < N; i++) {
            currentDiff += diff[i];
            A[i] += currentDiff;
            System.out.println(A[i]);
        }
    }
}




規則的な数列の和 

N, target = map(int, input().split())
numbers = list(map(int, input().split()))

# print(N, target, numbers)

left = 0
sums = 0
minlen = N+1 #pretent original is the smallest

for left in range(N):
    prod = 1
    for right in range(left, N):
        prod *= numbers[right]
        
        if prod == 0:
            break
        
        if prod >= target:
            minlen = min(minlen, right - left + 1)
        

print(minlen)


#ans from paiza
n, k = map(int, input().split())
numbers = list(map(int, input().split()))


def mul_list(data):
    result = 1
    for i in data:
        result *= i
    return result


count = float("inf")
start = 0
end = 0
while True:
    if end >= n or start > end:
        break
    if mul_list(numbers[start : end + 1]) >= k:
        if end - start + 1 < count:
            count = end - start + 1
        start += 1
    elif numbers[end] == 0:
        start = end + 1
        end += 1
    else:
        end += 1


print(count)


#java

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        long target = sc.nextLong();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int minLen = N + 1;

        for (int left = 0; left < N; left++) {
            long prod = 1;
            for (int right = left; right < N; right++) {
                prod *= A[right];

                if (prod == 0) {
                    break;
                }

                if (prod >= target) {
                    minLen = Math.min(minLen, right - left + 1);
                    break;
                }
            }
        }

        if (minLen > N) {
            System.out.println(-1);
        } else {
            System.out.println(minLen);
        }
    }
}